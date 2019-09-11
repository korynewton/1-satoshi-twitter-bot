import tweepy as tp
import os
import time
import random
import threading
import logging

from emoji_dict import *
from data import initial_retrieval, initialize_db, update_data, return_conn
from helpers import scheduled_tweet, fetch_price_data, regional_tweet, tweet_weakest
from settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_SECRET, ACCESS_TOKEN, FIXER_KEY, SYMBOL_KEY, NA_CURR, SA_CURR, EUR_CURR, AF_CURR, E_AS_CURR, SE_AS_CURR, C_AS_CURR, W_AS_CURR, S_AS_CURR


logFormatter = '%(asctime)s - %(levelname)s - %(message)s - %(details)s - %(currencies)s '
logging.basicConfig(format=logFormatter, level=logging.INFO,
                    filename='logging.log', filemode='w')
logger = logging.getLogger(__name__)


class Authentication:
    def __init__(self):
        self.auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    def handle_auth(self):
        return self.auth


class StdOutListener(tp.StreamListener):
    def __init__(self, api):
        # api with authentication
        self.api = api

    def on_error(self, status):
        print('error: ', status)

    def on_status(self, status):
        # print("on status")
        tweet = self.does_contain_currency(status.text)
        if tweet:
            for item in tweet:
                thread = threading.Thread(
                    target=self.compose, args=(status, item))
                thread.start()
                thread.join()

    def does_contain_currency(self, text):
        split = text.split(" ")
        currency = [i.upper() for i in split if len(i) ==
                    3 and i.upper() in SYMBOL_KEY]
        return currency

    def on_exception(self, exception):
        print(exception)
        return

    def get_price_data(self, curr):
        conn = return_conn()
        c = conn.cursor()

        query = 'SELECT currency,price from prices WHERE currency = (?)'
        c.execute(query, (curr,))

        data = c.fetchone()

        return data

    def compose(self, status, curr):
        emoji = emoji_dict[curr]

        price_data = self.get_price_data(curr)

        sats = float(price_data[1])

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

        if sats > 1:
            sats = '{0:.2f}'.format(sats)
        else:
            sats = '{0:.5f}'.format(sats)

        if hundred > 1:
            hundred = '{0:.2f}'.format(hundred)
        else:
            hundred = '{0:.5f}'.format(hundred)

        if thousand > 1:
            thousand = '{0:,.2f}'.format(thousand)
        else:
            thousand = '{0:.5f}'.format(thousand)

        if ten_thousand > 1:
            ten_thousand = '{0:,.2f}'.format(ten_thousand)
        else:
            ten_thousand = '{0:.5f}'.format(ten_thousand)

        if hundred_k > 1:
            hundred_k = '{0:,.2f}'.format(hundred_k)
        else:
            hundred_k = '{0:.5f}'.format(hundred_k)

        if million > 1:
            if million > 1000:
                million = '{:,d}'.format(round(million))
            else:
                million = '{0:.2f}'.format(million)
        else:
            million = '{0:.5f}'.format(million)

        # satoshi equivalent to currency
        if single_unit > 1:
            single_unit = '{:,d}'.format(round(single_unit))
        else:
            single_unit = '{0:.2f}'.format(single_unit)

        if ten_units > 100:
            ten_units = '{:,}'.format(round(ten_units))
        else:
            ten_units = '{0:.2f}'.format(ten_units)

        if hundred_units > 100:
            hundred_units = '{:,}'.format(round(hundred_units))
        else:
            hundred_units = '{0:.2f}'.format(hundred_units)

        if thousand_units > 100:
            thousand_units = '{:,}'.format(round(thousand_units))
        else:
            thousand_units = '{0:.2f}'.format(thousand_units)

        if five_hundred_units > 100:
            five_hundred_units = '{:,}'.format(round(five_hundred_units))
        else:
            five_hundred_units = '{0:.2f}'.format(five_hundred_units)

        if ten_thousand_units > 100:
            ten_thousand_units = '{:,}'.format(round(ten_thousand_units))
        else:
            ten_thousand_units = '{0:.2f}'.format(ten_thousand_units)

        if hundred_thousand_units > 100:
            hundred_thousand_units = '{:,}'.format(
                round(hundred_thousand_units))
        else:
            hundred_thousand_units = '{0:.2f}'.format(hundred_thousand_units)

        if hundredths_unit > 1:
            hundredths_unit = '{:,}'.format(round(hundredths_unit))
        else:
            hundredths_unit = '{0:.2f}'.format(hundredths_unit)

        larger_baseline = ['JPY', 'INR', 'KRW']
        if curr in larger_baseline:
            text = f'{emoji} ${curr} to #satoshi conversions:' + '\n' + \
                '\n' + f'   1 {curr} = {single_unit} sats' + \
                '\n' + f'   1,000 {curr} = {thousand_units} sats' + \
                '\n' + f'   10,000 {curr} = {ten_thousand_units} sats' + \
                '\n' + f'   100,000 {curr} = {hundred_thousand_units} sats' + \
                '\n' + '\n' + \
                '\n' + f'   1 sat = {sats} {curr}' + \
                '\n' + f'   100 sats = {hundred} {curr}' + \
                '\n' + f'   1,000 sats = {thousand} {curr}' + \
                '\n' + f'   1,000,000 sats = {million} {curr}' + \
                '\n' + '\n' + \
                f'1 #bitcoin = {bitcoin} {curr} {emoji}'
        else:
            text = f'{emoji} ${curr} to #satoshi conversions:' + '\n' + \
                '\n' + f'   .01 {curr} = {hundredths_unit} sats' + \
                '\n' + f'   1 {curr} = {single_unit} sats' + \
                '\n' + f'   100 {curr} = {hundred_units} sats' + \
                '\n' + f'   1,000 {curr} = {thousand_units} sats' + \
                '\n' + '\n' + \
                '\n' + f'   1 sat = {sats} {curr}' + \
                '\n' + f'   100 sats = {hundred} {curr}' + \
                '\n' + f'   10,000 sats = {ten_thousand} {curr}' + \
                '\n' + f'   1,000,000 sats = {million} {curr}' + \
                '\n' + '\n' + \
                f'   1 #bitcoin = {bitcoin} {curr} {emoji}'

        self.tweet(text, status.id)

    def tweet(self, text, reply_id):
        self.api.update_status(
            status=text, in_reply_to_status_id=reply_id, auto_populate_reply_metadata=True)
        logger.info('tweeted reply to:', extra={
                    'details': reply_id, 'currencies': ''})


if __name__ == "__main__":

    # If db exists, update with recent data
    # if it does not exist, initialize db
    if os.path.exists('data.db'):
        update_data()
    else:
        initialize_db()
        initial_retrieval()

    # authenticate tweepy
    auth = Authentication().handle_auth()
    api = tp.API(auth)

    # initialize stream
    listener = StdOutListener(api)
    stream = tp.Stream(auth, listener)

    print('streaming')
    stream.filter(track=['@1satoshibot show'], is_async=True)

    while True:
        num = random.randint(0, 10)

        if num == 0:
            # North America Regional Tweet
            tweet = scheduled_tweet(NA_CURR, 'NA')
        elif num == 1:
            # South America Regional Tweet
            tweet = scheduled_tweet(SA_CURR, 'SA')
        elif num == 2:
            # Europe Regional Tweet
            tweet = scheduled_tweet(EUR_CURR, 'EU')
        elif num == 3:
            # Africa Regional Tweet
            tweet = scheduled_tweet(AF_CURR, 'AF')
        elif num == 4:
            # Asia Regional Tweet
            tweet = scheduled_tweet(S_AS_CURR, "S_AS")
        elif num == 5:
            # SE Asia Regional Tweet
            tweet = scheduled_tweet(E_AS_CURR, "E_AS")
        elif num == 6:
            # SE Asia Regional Tweet
            tweet = scheduled_tweet(SE_AS_CURR, "SE_AS")
        elif num == 7:
            # SE Asia Regional Tweet
            tweet = scheduled_tweet(C_AS_CURR, "C_AS")
        elif num == 8:
            # SE Asia Regional Tweet
            tweet = scheduled_tweet(W_AS_CURR, "W_AS")
        elif num == 9:
            # Weakest currencies
            tweet = tweet_weakest()
        else:
            # Standard Random Tweet
            tweet = scheduled_tweet(SYMBOL_KEY)

        api.update_status(tweet)
        logger.info('Tweeted', extra={'currencies': '', 'details': ''})

        # wait between 50 and 80 minutes until next tweet
        wait = (50 * 60) + (random.randint(0, 30) * 60)
        print('scheduled tweet')
        logger.info(
            f"waiting {wait/60} minutes until next scheduled tweet",  extra={'currencies': '', 'details': ''})
        time.sleep(wait)
        update_data()
