import os, redis, re, time, tweepy as tp
from acronym_dict import SYMBOL_KEY
from datetime import datetime
from emoji_dict import emoji_dict

#Twitter credentials
CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

#Redis host
REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PW = os.environ["REDIS_PW"]
r = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True, password=REDIS_PW, socket_keepalive=True, retry_on_timeout=True)



#authenticate with Twitter
auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tp.API(auth)


class StdOutListener(tp.StreamListener):
    def on_status(self, status):
        # Check if tweet is not a retweet and contains a currency
        currencies = self.contains_currency(status.text)
        if self.is_not_retweet(status) and currencies:
            for currency in currencies:
                self.compose(status, currency)

    def on_exception(self, exception):
        print(exception)
        return

    def is_not_retweet(self, status):
        """checks if tweet is not a retweet"""
        try:
            return not hasattr(status, 'retweeted_status')
        except:
            return False

    def get_price_data(self, curr):
        price = r.get(curr)

        return price

    def contains_currency(self, text):
        all_matches = re.findall(r"(?=("+'|'.join(SYMBOL_KEY)+r"))", text)
        unique_matches = set(all_matches)

        return list(unique_matches)

    def compose(self, status, curr):
        emoji = emoji_dict[curr]

        price_data = self.get_price_data(curr)

        sats = float(price_data)

        hundred = sats * 100
        thousand = sats * 1000
        ten_thousand = sats * 10000
        hundred_k = sats * 100000
        million = sats * 1000000
        bitcoin = sats * 100000000

        single_unit = 1 / sats
        hundredths_unit = single_unit / 100
        ten_units = single_unit * 10
        hundred_units = single_unit * 100
        five_hundred_units = single_unit * 500
        thousand_units = single_unit * 1000
        ten_thousand_units = single_unit * 10000
        hundred_thousand_units = single_unit * 100000

        #  format numbers
        bitcoin = '{0:,}'.format(round(bitcoin))

        larger_baseline = ['JPY', 'KRW', 'IRR']
        if curr in larger_baseline:
            text = f'{emoji} ${curr} to #satoshi conversions:' + '\n' + \
                '\n' + f'  1 {curr} = {format_sats(single_unit)} sats' + \
                '\n' + f'  1,000 {curr} = {format_sats(thousand_units)} sats' + \
                '\n' + f'  10,000 {curr} = {format_sats(ten_thousand_units)} sats' + \
                '\n' + f'  100,000 {curr} = {format_sats(hundred_thousand_units)} sats' + \
                '\n' + '\n' + \
                '\n' + f'  1 sat = {format_currency(sats)} {curr}' + \
                '\n' + f'  100 sats = {format_currency(hundred)} {curr}' + \
                '\n' + f'  1,000 sats = {format_currency(thousand)} {curr}' + \
                '\n' + f'  1,000,000 sats = {format_currency(million)} {curr}' + \
                '\n' + '\n' + \
                f'1 #bitcoin = {bitcoin} {curr} {emoji}'
        else:
            text = f'{emoji} ${curr} to #satoshi conversions:' + '\n' + \
                '\n' + f'   .01 {curr} = {format_sats(hundredths_unit)} sats' + \
                '\n' + f'   1 {curr} = {format_sats(single_unit)} sats' + \
                '\n' + f'   100 {curr} = {format_sats(hundred_units)} sats' + \
                '\n' + f'   1,000 {curr} = {format_sats(thousand_units)} sats' + \
                '\n' + '\n' + \
                '\n' + f'   1 sat = {format_currency(sats)} {curr}' + \
                '\n' + f'   100 sats = {format_currency(hundred)} {curr}' + \
                '\n' + f'   10,000 sats = {format_currency(ten_thousand)} {curr}' + \
                '\n' + f'   1,000,000 sats = {format_currency(million)} {curr}' + \
                '\n' + '\n' + \
                f'   1 #bitcoin = {bitcoin} {curr} {emoji}'

        self.tweet(text, status.id)

    def tweet(self, text, reply_id):
        self.api.update_status(
            status=text, in_reply_to_status_id=reply_id, auto_populate_reply_metadata=True)
        print(f"Successful response to: {reply_id} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
def format_currency(amount):
    return '{0:,.2f}'.format(amount) if amount > 1 else '{0:.2g}'.format(amount)

def format_sats(amount):
    return '{:,}'.format(round(amount)) if amount > 1 else '{0:.2g}'.format(amount)

if __name__ == "__main__":
    while True:
        try:
            print("starting stream...")
            #initialize listener and start stream
            listener = StdOutListener(api)
            stream = tp.Stream(auth, listener)
            stream.filter(track=['@1satoshibot show'])
        except Exception as e:
            print("error at: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), " waiting 30 seconds before next attempt")
            print("error: ", e)
        time.sleep(30)
