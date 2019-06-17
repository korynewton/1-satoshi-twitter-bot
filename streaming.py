import tweepy as tp
from settings import *


# twitter credentials
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_secret = ACCESS_SECRET
fixer_key = FIXER_KEY

# override tweepy.StreamListener to add logic to on_status


class MyStreamListener(tp.StreamListener):

    def on_status(self, status):
        print(status.text)
        self.compose(status)

    def compose(self, status):
        pass


auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

myStreamListener = MyStreamListener()
myStream = tp.Stream(auth=api.auth, listener=myStreamListener)


myStream.filter(track=['@1satoshibot'], is_async=True)

# my user id
# myStream.filter(follow=["1035658046515466240"])
