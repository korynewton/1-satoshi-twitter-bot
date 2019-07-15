import tweepy as tp
import time

from settings import *
from streaming import MyStreamListener
from scheduled_tweet import (getData, compose, tweet)


# twitter credentials
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_secret = ACCESS_SECRET
fixer_key = FIXER_KEY


if __name__ == "__main__":
    # Initialize stream
    myStreamListener = MyStreamListener()
    myStream = tp.Stream(auth=myStreamListener.api.auth,
                         listener=myStreamListener)
    myStream.filter(track=['1satoshibot'], is_async=True)

    while True:
        getData()
        wait = 30 * 60
        time.sleep(wait)
        print(f'waited {wait} seconds')
