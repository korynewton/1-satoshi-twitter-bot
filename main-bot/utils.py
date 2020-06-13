import random, json
from emoji_dict import emoji_dict


#all currencies
SYMBOL_KEY = ['GBP', 'JPY', 'EUR', 'USD', 'KZT', 'AUD', 'CAD', 'INR', 'RUB',
              'TRY', 'VES', 'ZWL', 'MXN', 'ARS', 'AOA', 'BRL', 'ZAR', 'LRD',
              'LYD', 'LSL', 'NAD', 'SZL', 'MMK', 'SEK', 'PKR', 'NPR',
              'BTN', 'AED', 'AFN', 'ALL', 'AMD', 'BDT', 'AWG', 'AZN',
              'BAM', 'BBD', 'BGN', 'BHD', 'BIF', 'BND', 'BOB', 'BSD', 'BMD',
              'BWP', 'BYN', 'BZD', 'XAF', 'CDF', 'CHF', 'CLP', 'CNY', 'COP',
              'CRC', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN',
              'ETB', 'FJD', 'FKP', 'GEL', 'GGP', 'GHS', 'GIP', 'GNF', 'GTQ',
              'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IQD',
              'ISK', 'JMD', 'JOD', 'KES', 'KGS', 'KHR', 'KMF', 'KRW',
              'KWD', 'KYD', 'LAK', 'LBP', 'LKR', 'MAD', 'MDL', 'MGA', 'MKD',
              'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MYR', 'MZN',
              'NGN', 'NIO', 'NOK', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP',
              'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RWF', 'SAR', 'SBD', 'SCR',
              'SLL', 'SOS', 'SRD', 'STD', 'THB', 'TJS', 'TMT', 'TND',
              'TOP', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VND',
              'VUV', 'WST', 'YER', 'ZMW', 'CUP', 'KPW', 'SYP', 'SDG', 'IRR',
              'BYR', 'GMD', 'ANG', 'CNH', 'EEK', 'IMP', 'SGD', 'SHP', 'SSP']

# North America currencies
NA_CURR = ['USD', 'MXN', 'CAD', 'NIO', 'JMD', 'HTG', 'HNL', 'GTQ',
           'DOP', 'CUP', 'CRC', 'KYD', 'BMD', 'BZD', 'BBD', 'BSD',
           'AWG', 'ANG', 'TTD']

# South America currencies
SA_CURR = ['ARS', 'BOB', 'BRL', 'CLP', 'COP', 'FKP', 'GYD',
           'PYG', 'PEN', 'SRD', 'UYU', 'VES', 'USD', 'EUR',
           'PAB']

# European currencies
EUR_CURR = ['EUR', 'GBP', 'ALL', 'AMD', 'AZN', 'BYN', 'BAM',
            'BGN', 'HRK', 'CZK', 'DKK', 'GEL', 'HUF', 'ISK',
            'CHF', 'MDL', 'MKD', 'NOK', 'PLN', 'RON',
            'RSD', 'SEK', 'TRY', 'UAH', 'EEK', 'IMP', 'GGP',
            'GIP', 'BYR']

# African currencies
AF_CURR = ['NGN', 'KES', 'BWP', 'EGP', 'RWF', 'GHS', 'MWK',
           'MUR', 'MAD', 'ZAR', 'TZS', 'UGX', 'ZMW', 'NAD',
           'DZD', 'AOA', 'BIF', 'CVE', 'KMF', 'CDF', 'XAF',
           'DJF', 'ERN', 'SZL', 'ETB', 'GMD', 'GNF', 'LSL',
           'LRD', 'LYD', 'MGA', 'MZN', 'SCR', 'SLL', 'SOS',
           'SDG', 'SSP', 'ZWL', 'TND', 'MRO', 'STD']

# South Asia
S_AS_CURR = ['AFN', 'BDT', 'BTN', 'INR', 'MVR', 'NPR', 'PKR', 'LKR']

# East Asia
E_AS_CURR = ['CNY', 'JPY', 'MNT', 'KPW', 'KRW', 'TWD', 'HKD', 'MOP', 'CNH']

# South East Asia
# missing countries: East Timor (USD)
SE_AS_CURR = ['AUD', 'BND', 'KHR', 'IDR', 'LAK',
              'MYR', 'MMK', 'PHP', 'THB', 'VND',
              'SGD', 'FJD', 'PGK', 'SBD', 'TOP',
              'VUV', 'WST', 'NZD']

# Centra Asia currencies
C_AS_CURR = ['KZT', 'KGS', 'TJS', 'TMT', 'UZS', 'RUB']

# Middle East currencies
W_AS_CURR = ['AED', 'BHD', 'ILS', 'IQD', 'JOD', 'KWD',
             'LBP', 'OMR', 'QAR', 'SAR', 'YER', 'SYP',
             'IRR']



def tweet_weakest():
    '''todo after setting up redis container'''
    pass


def get_price_info(selected):
    with_data = []

    for curr in selected:
        with_data.append([curr, .0004])
    # conn = sqlite3.connect('data.db')
    # c = conn.cursor()

    # placeholder = '?'
    # placeholders = ', '.join(placeholder for _ in selected)
    # query = 'SELECT currency, price from prices WHERE currency IN (%s)' % placeholders

    # with_data = c.execute(query, selected).fetchall()

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

    to_be_tweeted += '                       #Bitcoin'
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



