import tweepy as tp
import random,time
from settings import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET

# Authenticate
auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tp.API(auth)

# sleep
print("daily script started")
hours = random.randint(1,4) * 60 * 60
minutes = random.randint(1,60)*60
total_sleep = hours + minutes
print(f"sleeping for {total_sleep} seconds...")
time.sleep(hours+minutes)

#select currency from list and tweet
daily_show = ['USD', 'CAD', 'JPY', 'CNY', 'MXN', 'RUB', 'EUR', 'AUD', 'INR']
currency = random.choice(daily_show)
tweet = f"@1satoshibot show {currency}"

try:
    print(f"tweeting: {tweet}")
    api.update_status(tweet)
except:
    print(f'error tweeting daily (Currency={currency}')


