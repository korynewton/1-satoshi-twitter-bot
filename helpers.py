import random
from emoji_dict import *
from settings import FIXER_KEY
import requests
import sqlite3


def get_price_info(selected):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    placeholder = '?'
    placeholders = ', '.join(placeholder for unused in selected)
    query = 'SELECT currency, price from prices WHERE currency IN (%s)' % placeholders

    with_data = c.execute(query, selected).fetchall()

    return with_data


def compose_scheduled_tweet(selected):
    to_be_tweeted = '1 #satoshi =        '

    for i in range(len(selected)):
        curr = selected[i][0]
        price = selected[i][1]
        emoji = emoji_dict[curr]
        price = '{0:.5f}'.format(price)

        if i == 0:
            to_be_tweeted += str(price) + ' $' + curr + ' ' + emoji + '\n'

        elif i % 2 != 0:
            to_be_tweeted += str(price) + ' $' + curr + ' ' + emoji

        else:
            to_be_tweeted += '   ' + \
                str(price) + ' $' + curr + ' ' + emoji + '\n'

    to_be_tweeted = to_be_tweeted + \
        '                       ' + '#Bitcoin'

    return to_be_tweeted


def scheduled_tweet():
    symbol_key = ['GBP', 'JPY', 'EUR', 'USD', 'KZT', 'AUD', 'CAD', 'INR', 'RUB', 'TRY', 'VES', 'ZWL', 'MXN', 'ARS', 'AOA', 'BRL', 'ZAR', 'LRD', 'LYD', 'LSL', 'NAD', 'SZL', 'TND', 'MMK', 'SEK', 'PKR', 'NPR', 'BTN', 'AED', 'AFN', 'ALL', 'AMD', 'AOA', 'BDT', 'AWG', 'AZN', 'BAM', 'BBD', 'BGN', 'BHD', 'BIF', 'BND', 'BOB', 'BSD', 'BMD', 'BWP', 'BYN', 'BZD', 'XAF', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'FJD', 'FKP', 'GEL', 'GGP', 'GHS', 'GIP', 'GNF', 'GTQ', 'GYD',
                  'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IQD', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD', 'LAK', 'LBP', 'LKR', 'MAD', 'MDL', 'MGA', 'MKD', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RWF', 'SAR', 'SBD', 'SCR', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VND', 'VUV', 'WST', 'YER', 'ZMW', 'CUP', 'KPW', 'SYP', 'SDG', 'IRR', 'BYR', 'GMD']

    # Select currencies at random
    random_select = random.sample(symbol_key, 13)

    # retrieve data from database
    select_with_data = get_price_info(random_select)
    random.shuffle(select_with_data)

    # compose tweet
    tweet = compose_scheduled_tweet(select_with_data)

    return tweet


def update_data():
    rates_data = {}
    fixer_url = 'http://data.fixer.io/api/latest?access_key=' + \
        FIXER_KEY + '&base=EUR&symbols=BTC,EUR, SDG, CUP, KPW, SYP, IRR'
    url = 'https://api.coinbase.com/v2/exchange-rates?currency=BTC'
    try:
            # retrieve data from coinbase and fixer apis
        cb_json_data = requests.get(url).json()['data']['rates']
        fixer_json_data = requests.get(fixer_url).json()['rates']

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

    except:
        print('fixer or coinbase request failed')
