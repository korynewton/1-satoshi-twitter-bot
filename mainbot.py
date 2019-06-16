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
    random_select = {}
    fixer_url = 'http://data.fixer.io/api/latest?access_key=' + \
        fixer_key + '&base=EUR&symbols=BTC,EUR, SDG, CUP, KPW, SYP'
    url = 'https://api.coinbase.com/v2/exchange-rates?currency=BTC'
    try:
        cb_json_data = requests.get(url).json()['data']['rates']
        fixer_json_data = requests.get(fixer_url).json()['rates']

        for key in emoji_dict:
            if key in cb_json_data:
                price_sats = float(cb_json_data[key])
                rates_data[key] = str(price_sats / 100000000)

        EUR = fixer_json_data['EUR']
        BTC = fixer_json_data['BTC']
        bitprice = (EUR / BTC)
        fixer_json_data.update((x, y*bitprice / 100000000)
                               for x, y in fixer_json_data.items())
        for key in fixer_json_data:
            if not key == 'BTC' and not key == 'EUR':
                rates_data[key] = str(fixer_json_data[key])

        print(rates_data)

    except:
        print('request failed')

    for key in rates_data:
        rates_data[key] = float(rates_data[key])

    # print(rates_data)
    random_select = random.sample(symbol_key, 12)

    compose(random_select)


def compose(randomly_selected):
    to_be_tweeted = ''
    print(randomly_selected)
    # global to_be_tweeted
    for i in range(len(randomly_selected)):
        key = randomly_selected[i]
        emoji = emoji_dict[key]
        price = '{0:.5f}'.format(rates_data[key])
        if i % 2 == 0:
            even_line = '\n' + emoji + ': ' + str(price) + ' ' + key
            to_be_tweeted = to_be_tweeted + even_line
        else:
            odd_line = '   ' + emoji + ': ' + str(price) + ' ' + key
            to_be_tweeted = to_be_tweeted + odd_line
        i += 1
    to_be_tweeted = to_be_tweeted + '\n' + '                       #Bitcoin'
    print(to_be_tweeted)
    tweet(to_be_tweeted)


# tweet
def tweet(tweet_text):
    api.update_status(tweet_text)
    print('tweeted')
    time.sleep(5400)
    getData()


getData()
