import tweepy as tp
import time
import random
from urllib3.exceptions import ProtocolError

from settings import *
from streaming import MyStreamListener
from scheduled_tweet import ScheduledTweet
from data import Retrieve_Data


# twitter credentials
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_secret = ACCESS_SECRET
fixer_key = FIXER_KEY


if __name__ == "__main__":
    # Initialize stream to listen for mentions
    myStreamListener = MyStreamListener()
    myStream = tp.Stream(auth=myStreamListener.api.auth,
                         listener=myStreamListener)
    while True:
        try:
            myStream.filter(track=['usd'], is_async=True)
        except (ProtocolError, AttributeError) as e:
            print(e)
            continue

        while True:
            # Retrieve_Data()
            ScheduledTweet()
            wait = 50 * 60 + (random.randint(1, 30) * 60)
            print(f'waiting {wait} seconds')
            time.sleep(wait)
