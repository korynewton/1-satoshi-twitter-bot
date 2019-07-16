import requests
import time
import random
import pickle

from settings import *
from emoji_dict import *


fixer_key = FIXER_KEY


class Retrieve_Data():
    def __init__(self):
        self.get_data()

    def get_data(self):
        rates_data = {}
        fixer_url = 'http://data.fixer.io/api/latest?access_key=' + \
            fixer_key + '&base=EUR&symbols=BTC,EUR, SDG, CUP, KPW, SYP, IRR'
        url = 'https://api.coinbase.com/v2/exchange-rates?currency=BTC'
        try:
            # retrieve data from coinbase and fixer apis
            cb_json_data = requests.get(url).json()['data']['rates']
            fixer_json_data = requests.get(fixer_url).json()['rates']

            # print(cb_json_data)
            print('USD:', cb_json_data['USD'])

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

            pickle_out = open('price_data.txt', 'wb')
            pickle.dump(rates_data, pickle_out)
            pickle_out.close()

            # print(rates_data)

        except:
            print('request failed')
            time.sleep(1000)
            self.get_data()
