import tweepy as tp
import random
from settings import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET

# Authenticate
auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tp.API(auth)


daily_show = ['USD', 'CAD', 'JPY', 'CNY', 'MXN', 'RUB', 'EUR', 'AUD', 'INR']
currency = random.choice(daily_show)
try:
    api.update_status(f"@1satoshibot show {currency}")
except:
    print(f'error tweeting daily (Currency={currency}')


