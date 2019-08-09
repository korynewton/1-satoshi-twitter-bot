import tweepy as tp
import os
import time
import random
from settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_SECRET, ACCESS_TOKEN, FIXER_KEY
from helpers import compose_scheduled_tweet, update_data


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


def scheduled_tweet():
    pass


if __name__ == "__main__":
    auth = Authentication().handle_auth()
    api = tp.API(auth)

    listener = StdOutListener()
    stream = tp.Stream(auth, listener)

    stream.filter(track=["@1satoshibot"], is_async=True)

    while True:
        update_data()
        print('***** while loop ********* : ')
        tweet = compose_scheduled_tweet()
        # api.update_status(tweet)

        # wait between 50 and 80 minutes until next tweet
        wait = 50 * 60 + (random.randint(1, 30) * 60)
        time.sleep(wait)
