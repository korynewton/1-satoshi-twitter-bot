import random, redis, os
from emoji_dict import emoji_dict
from acronym_dict import *

REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PW = os.environ["REDIS_PW"]
r = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True, password=REDIS_PW, socket_keepalive=True, retry_on_timeout=True)


def tweet_weakest():
    # get all redis keys (currency acronyms)
    all_keys = r.keys('*')
    #get all prices
    data = r.mget(all_keys)
    #combine keys with prices
    with_data = [[all_keys[i], data[i]] for i in range(len(all_keys))]
    #sort by price
    with_data.sort(key=lambda x:float(x[1]), reverse=True)

    tweet = compose_scheduled_tweet(with_data[:13])

    return tweet

def get_price_info(selected):
    data = r.mget(selected)
    with_data = []

    for i in range(len(selected)):
        with_data.append([selected[i], data[i]])

    return with_data


def compose_scheduled_tweet(selected):
    to_be_tweeted = '1 #satoshi =        '

    for i in range(len(selected)):
        curr = selected[i][0]
        price = selected[i][1]
        emoji = emoji_dict[curr]

        price = '{0:.5f}'.format(float(price))

        if i == 0:
            to_be_tweeted += price + ' $' + curr + ' ' + emoji + '\n'

        elif i % 2 != 0:
            to_be_tweeted += price + ' $' + curr + ' ' + emoji

        else:
            to_be_tweeted += ' ' + \
                price + ' $' + curr + ' ' + emoji + '\n'

    to_be_tweeted += '                      #Bitcoin'
    return to_be_tweeted


def scheduled_tweet(currencies, region_name=None):
    _global = ['USD', 'EUR']
    max_num = 13 if len(currencies) > 13 else len(currencies)

    # Select currencies at random
    selected = random.sample(currencies, max_num)


    # ensure there is 13 currencies
    if region_name == 'S_AS':
        selected += _global
        iterator = random.randint(0, len(C_AS_CURR)-1)
        while len(selected) < 13:
            selected.append(C_AS_CURR[iterator])
            iterator = (iterator + 1) % len(C_AS_CURR)
    elif region_name in ['C_AS', 'E_AS']:
        selected += _global
        iterator = random.randint(0, len(S_AS_CURR)-1)
        while len(selected) < 13:
            selected.append(S_AS_CURR[iterator])
            iterator = (iterator + 1) % len(S_AS_CURR)


    # retrieve data from database
    select_with_data = get_price_info(selected)
    random.shuffle(select_with_data)

    # compose tweet
    tweet = compose_scheduled_tweet(select_with_data)

    return tweet



def regional_tweet(currencies):
    # select 13 currencies from the region
    random_select = random.sample(currencies, 13)

    # get price data from database then shuffle the order
    select_with_data = get_price_info(random_select)
    random.shuffle(select_with_data)

    # compose tweet
    tweet = compose_scheduled_tweet(select_with_data)

    return tweet



