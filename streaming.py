import tweepy as tp
from settings import *
from emoji_dict import *
import pickle


# twitter credentials
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_secret = ACCESS_SECRET
fixer_key = FIXER_KEY

# import current price data from file
pickle_in = open('price_data.txt', 'rb')
price_data = pickle.load(pickle_in)


# override tweepy.StreamListener to add logic to on_status


class MyStreamListener(tp.StreamListener):

    def on_status(self, status):
        # filter
        split = status.text.split()
        currency = [i for i in split if len(i) == 3]
        for item in currency:
            if item in price_data:
                self.compose(status, item)

    def compose(self, status, curr):
        emoji = emoji_dict[curr]

        sats = float(price_data[curr])
        hundred = sats * 100
        thousand = sats * 1000
        hundred_k = sats * 100000
        million = sats * 1000000

        single_unit = 1 / sats
        ten_units = single_unit * 10
        hundred_units = single_unit * 100
        thousand_units = single_unit * 1000

        #  format numbers
        if sats > 1:
            sats = '{0:.2f}'.format(sats)
        else:
            sats = '{0:.5f}'.format(sats)

        if hundred > 1:
            hundred = '{0:.2f}'.format(hundred)
        else:
            hundred = '{0:.5f}'.format(hundred)

        if thousand > 1:
            thousand = '{0:.2f}'.format(thousand)
        else:
            thousand = '{0:.5f}'.format(thousand)

        if hundred_k > 1:
            hundred_k = '{0:.2f}'.format(hundred_k)
        else:
            hundred_k = '{0:.5f}'.format(hundred_k)

        if million > 1:
            million = '{0:.2f}'.format(million)
        else:
            million = '{0:.5f}'.format(million)

        if single_unit > 1:
            single_unit = '{:,d}'.format(round(single_unit))
        else:
            single_unit = '{0:.5f}'.format(single_unit)

        if ten_units > 1:
            ten_units = '{:,}'.format(round(ten_units))
        else:
            ten_units = '{0:.5f}'.format(ten_units)

        if hundred_units > 1:
            hundred_units = '{:,}'.format(round(hundred_units))
        else:
            hundred_units = '{0:.5f}'.format(hundred_units)

        if thousand_units > 1:
            thousand_units = '{:,}'.format(round(thousand_units))
        else:
            thousand_units = '{0:.5f}'.format(thousand_units)

            # '\n' + f'100,000 #satoshis = {hundred_k} ${curr}' + \
        text = '      ' + emoji + \
            '\n' + f'1 #satoshi = {sats} ${curr}' + \
            '\n' + f'100 #satoshis = {hundred} ${curr}' + \
            '\n' + f'1,000 #satoshis = {thousand} ${curr}' + \
            '\n' + f'1,000,000 #satoshis = {million} ${curr}' + \
            '\n' + '------------------------------------' + \
            '\n' + f'1 ${curr} = {single_unit} #satoshis' + \
            '\n' + f'10 ${curr} = {ten_units} #satoshis' + \
            '\n' + f'100 ${curr} = {hundred_units} #satoshis' + \
            '\n' + f'1,000 ${curr} = {thousand_units} #satoshis'
        # print(text)
        # self.update_status(text, status.id)
        self.tweet_it(text, status.id)

    def tweet_it(self, text, reply_id):
        # reply_id = str(reply_id)
        api.update_status(
            status=text, in_reply_to_status_id=reply_id, auto_populate_reply_metadata=True)
        # api.update_status(status,)
        print('reply ID:', reply_id)
        print('tweeted')


auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

myStreamListener = MyStreamListener()
myStream = tp.Stream(auth=api.auth, listener=myStreamListener)


myStream.filter(track=['@1satoshibot'], is_async=True)

# my user id
# myStream.filter(follow=["1035658046515466240"])
