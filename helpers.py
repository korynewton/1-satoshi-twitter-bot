import random
from emoji_dict import *
import pickle
from settings import FIXER_KEY
import time
import requests


def compose_scheduled_tweet():
    pickle_in = open('price_data.txt', 'rb')
    rates_data = pickle.load(pickle_in)
    symbol_key = ['GBP', 'JPY', 'EUR', 'USD', 'KZT', 'AUD', 'CAD', 'INR', 'RUB', 'TRY', 'VES', 'ZWL', 'MXN', 'ARS', 'AOA', 'BRL', 'ZAR', 'LRD', 'LYD', 'LSL', 'NAD', 'SZL', 'TND', 'MMK', 'SEK', 'PKR', 'NPR', 'BTN', 'AED', 'AFN', 'ALL', 'AMD', 'AOA', 'BDT', 'AWG', 'AZN', 'BAM', 'BBD', 'BGN', 'BHD', 'BIF', 'BND', 'BOB', 'BSD', 'BMD', 'BWP', 'BYN', 'BZD', 'XAF', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'FJD', 'FKP', 'GEL', 'GGP', 'GHS', 'GIP', 'GNF', 'GTQ', 'GYD',
                  'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IQD', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD', 'LAK', 'LBP', 'LKR', 'MAD', 'MDL', 'MGA', 'MKD', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RWF', 'SAR', 'SBD', 'SCR', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VND', 'VUV', 'WST', 'YER', 'ZMW', 'CUP', 'KPW', 'SYP', 'SDG', 'IRR', 'BYR', 'GMD']

    # Select currencies at random
    random_select = random.sample(symbol_key, 13)

    to_be_tweeted = '1 #satoshi =        '
    print(random_select)
    for i in range(len(random_select)):
        key = random_select[i]
        emoji = emoji_dict[key]
        price = '{0:.5f}'.format(rates_data[key])

        if i == 0:
            to_be_tweeted += str(price) + ' $' + key + ' ' + emoji + '\n'

        elif i % 2 != 0:
            to_be_tweeted += str(price) + ' $' + key + ' ' + emoji

        else:
            to_be_tweeted += '   ' + \
                str(price) + ' $' + key + ' ' + emoji + '\n'

    to_be_tweeted = to_be_tweeted + \
        '                       ' + '#Bitcoin'

    return to_be_tweeted


def update_data():
    rates_data = {}
    fixer_url = 'http://data.fixer.io/api/latest?access_key=' + \
        FIXER_KEY + '&base=EUR&symbols=BTC,EUR, SDG, CUP, KPW, SYP, IRR'
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

    except:
        print('fixer or coinbase request failed')
        time.sleep(1000)
        update_data()
