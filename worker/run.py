import os, redis, time, requests, json
from datetime import datetime
from emoji_dict import emoji_dict

FIXER_KEY = os.environ["FIXER_KEY"]

REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PW = os.environ["REDIS_PW"]
r = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True, password=REDIS_PW, socket_keepalive=True, retry_on_timeout=True)

def fetch_price_data():
    fixer_url = 'http://data.fixer.io/api/latest?access_key=' + \
        FIXER_KEY + '&base=EUR&symbols=BTC,EUR, SDG, CUP, KPW, SYP, IRR'
    coinbase_url = 'https://api.coinbase.com/v2/exchange-rates?currency=BTC'
    try:
            # retrieve data from coinbase and fixer apis
        cb_json_data = requests.get(coinbase_url).json()['data']['rates']
        fixer_json_data = requests.get(fixer_url).json()['rates']

        rates_data = {}
        # from cb data, store data there are emojis for in rates_data, convert to sats
        for key in emoji_dict:
            if key in cb_json_data:
                price_sats = float(cb_json_data[key])
                rates_data[key] = str(price_sats / 100000000)

        # for fixer data, get conversion based on EUR/BTC pair, multiply fixer currency with conversion rate
        EUR = fixer_json_data['EUR']
        BTC = fixer_json_data['BTC']
        bitprice = (EUR / BTC)

        fixer_json_data.update((x, y*bitprice / 100000000)
                               for x, y in fixer_json_data.items())
        for key in fixer_json_data:
            if not key == 'BTC' and not key == 'EUR':
                rates_data[key] = str(fixer_json_data[key])

        for key in rates_data:
            rates_data[key] = float(rates_data[key])

        return rates_data

    except Exception as e:
        print("error at: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), e)



def update_data():
    #fetch data
    data = fetch_price_data()
    #set data
    r.mset(data)
        


if __name__ == "__main__":
    
    while True:
        try:
            update_data()
            # sleep for hour
            print("data updated at ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            time.sleep(60*60)
        except Exception as e:
            print("error at: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), e)
            #sleep for 10 seconds and try again
            time.sleep(10)

        

