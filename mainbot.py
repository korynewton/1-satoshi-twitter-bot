# @1satoshibot
import requests
import random
import tweepy as tp
import time
from settings import *
from emoji_dict import *


# twitter credentials
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_secret = ACCESS_SECRET
fixer_key = FIXER_KEY

# login to twitter
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)


symbol_key = ['GBP', 'JPY', 'EUR', 'USD', 'KZT', 'AUD', 'CAD', 'INR', 'RUB', 'TRY', 'VES', 'ZWL', 'MXN', 'ARS', 'AOA', 'BRL', 'ZAR', 'LRD', 'LYD', 'LSL', 'NAD', 'SZL', 'TND', 'MMK', 'SEK', 'PKR', 'NPR', 'BTN', 'AED', 'AFN', 'ALL', 'AMD', 'AOA', 'BDT', 'AWG', 'AZN', 'BAM', 'BBD', 'BGN', 'BHD', 'BIF', 'BND', 'BOB', 'BSD', 'BMD', 'BWP', 'BYN', 'BZD', 'XAF', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'FJD', 'FKP', 'GEL', 'GGP', 'GHS', 'GIP', 'GNF', 'GTQ', 'GYD',
              'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IQD', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD', 'LAK', 'LBP', 'LKR', 'MAD', 'MDL', 'MGA', 'MKD', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RWF', 'SAR', 'SBD', 'SCR', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VND', 'VUV', 'WST', 'YER', 'ZMW', 'CUP', 'KPW', 'SYP', 'SDG']


rates_data = {}


def getData():
    fixer_url = 'http://data.fixer.io/api/latest?access_key=' + \
        fixer_key + '&base=EUR&symbols=BTC,EUR, SDG, CUP, KPW, SYP'
    url = 'https://api.coinbase.com/v2/exchange-rates?currency=BTC'
    try:
        # retrieve data from coinbase and fixer apis
        cb_json_data = requests.get(url).json()['data']['rates']
        fixer_json_data = requests.get(fixer_url).json()['rates']

        print(cb_json_data)

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

        # write data to file for access from other threads
        data_file = open('data_file.txt', 'w')
        data_file.write(repr(rates_data))
        data_file.close()

        # print(rates_data)

    except:
        print('request failed')
        time.sleep(1000)
        getData()

    for key in rates_data:
        rates_data[key] = float(rates_data[key])

    # Select currencies at random
    random_select = random.sample(symbol_key, 13)

    compose(random_select)


def compose(randomly_selected):
    hashtag = ['#Bitcoin', '#StackingSats']
    to_be_tweeted = '1 #satoshi =        '
    print(randomly_selected)
    for i in range(len(randomly_selected)):
        key = randomly_selected[i]
        emoji = emoji_dict[key]
        price = '{0:.5f}'.format(rates_data[key])

        if i == 0:
            to_be_tweeted += emoji + ': ' + str(price) + ' ' + key + '\n'

        elif i % 2 != 0:
            to_be_tweeted += emoji + ': ' + str(price) + ' ' + key
        else:
            to_be_tweeted += '   ' + emoji + \
                ': ' + str(price) + ' ' + key + '\n'

    to_be_tweeted += '                       ' + random.choice(hashtag)
    print(to_be_tweeted)
    tweet(to_be_tweeted)


# tweet
def tweet(tweet_text):
    api.update_status(tweet_text)
    print('tweeted')
    time.sleep(5400)
    getData()


getData()
