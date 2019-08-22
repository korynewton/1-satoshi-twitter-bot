import tweepy as tp
import os
import time
import random
from data import initial_retrieval, initialize_db, update_data

from settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_SECRET, ACCESS_TOKEN, FIXER_KEY
from helpers import scheduled_tweet, fetch_price_data


class Authentication:
    def __init__(self):
        self.auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    def handle_auth(self):
        return self.auth


class StdOutListener(tp.StreamListener):
    def on_error(self, status):
        print('error: ', status)

    def on_status(self, status):
        print('tweet: ', status)

        # TODO handle composing and tweeting when bot is mentioned


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
    listener = StdOutListener()
    stream = tp.Stream(auth, listener)

    stream.filter(track=['@1satoshibot'], is_async=True)

    while True:
        print('***** while loop ********* : ')
        tweet = scheduled_tweet()
        print(tweet)
        # api.update_status(tweet)

        # wait between 50 and 80 minutes until next tweet
        wait = (50 + (random.randint(1, 30)) * 60)
        time.sleep(wait)
        update_data()
