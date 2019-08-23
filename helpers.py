import random
from emoji_dict import *
from settings import FIXER_KEY, SYMBOL_KEY
import requests
import sqlite3


def get_price_info(selected):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    placeholder = '?'
    placeholders = ', '.join(placeholder for _ in selected)
    query = 'SELECT currency, price from prices WHERE currency IN (%s)' % placeholders

    with_data = c.execute(query, selected).fetchall()

    return with_data


def compose_scheduled_tweet(selected, region=None):
    n_america_hashtags = ['#NorthAmerica', '#Norteamérica']
    s_america_hashtags = ['#SouthAmerica', '#Sudamérica']
    eur_hashtags = ["#Европа", "#Europa",
                    "#LEurope", "#Europe", "#Avrupa", "#Європа"]
    africa_hashtags = ['#Afrika', '#Africa', '#አፍሪካ', '#Afirika', '#Afrịka']

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

    if region:
        if region == "North America":
            random.shuffle(n_america_hashtags)
            for i in range(2):
                to_be_tweeted += f"{n_america_hashtags[i]} "
        elif region == "South America":
            random.shuffle(s_america_hashtags)
            for i in range(2):
                to_be_tweeted += f"{s_america_hashtags[i]} "
        elif region == "Europe":
            random.shuffle(eur_hashtags)
            for i in range(2):
                to_be_tweeted += f"{eur_hashtags[i]} "
        elif region == "Africa":
            random.shuffle(africa_hashtags)
            for i in range(2):
                to_be_tweeted += f"{africa_hashtags[i]} "

    to_be_tweeted += "#Bitcoin"
    return to_be_tweeted


def scheduled_tweet():
    symbol_key = SYMBOL_KEY

    # Select currencies at random
    random_select = random.sample(symbol_key, 13)

    print(random_select)

    # retrieve data from database
    select_with_data = get_price_info(random_select)
    random.shuffle(select_with_data)

    # compose tweet
    tweet = compose_scheduled_tweet(select_with_data)

    return tweet


def fetch_price_data():
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


def regional_tweet(currencies, region):
    # select 13 currencies from the region
    random_select = random.sample(currencies, 13)

    # get price data from database then shuffle the order
    select_with_data = get_price_info(random_select)
    random.shuffle(select_with_data)

    # compose tweet
    tweet = compose_scheduled_tweet(select_with_data, region)

    return tweet
