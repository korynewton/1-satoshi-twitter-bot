import os, time, random, tweepy as tp
from datetime import datetime
from acronym_dict import *
from utils import scheduled_tweet, tweet_weakest

#Twitter credentials
CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

#authenticate
auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tp.API(auth)

while True:
    try:
        #choose a random number between 0 - 10 to choose which region will be tweeted
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
        # wait between 120 and 200 min
        wait = (120 + random.randint(0, 80)) * 60
        print(f"Tweeted successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, waiting {wait/60} mins...")
        time.sleep(wait)
    except Exception as e:
        print("error at: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("error details: ", e)
        print("Number selected: ", num)
        print("Error tweet: ", tweet)
        time.sleep(10)
        continue