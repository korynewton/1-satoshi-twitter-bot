import random

# emoji dictionary with currency symbole as key and emoji code as value
emoji_dict = {'GBP': '\U0001F1EC\U0001F1E7', 'JPY': '\U0001F1EF\U0001F1F5',
              'EUR': '\U0001F1EA\U0001F1FA', 'USD': '\U0001F1FA\U0001F1F8', 'KZT': '\U0001F1F0\U0001F1FF',
              'AUD': '\U0001F1E6\U0001F1FA', 'CAD': '\U0001F1E8\U0001F1E6', 'INR': '\U0001F1EE\U0001F1F3',
              'RUB': '\U0001F1F7\U0001F1FA', 'TRY': '\U0001F1F9\U0001F1F7', 'VES': '\U0001F1FB\U0001F1EA',
              'ZWL': '\U0001F1FF\U0001F1FC', 'MXN': '\U0001F1F2\U0001F1FD', 'IRR': '\U0001F1EE\U0001F1F7',
              'SDG': '\U0001F1F8\U0001F1E9', 'ARS': '\U0001F1E6\U0001F1F7', 'AOA': '\U0001F1E6\U0001F1F4',
              'BRL': '\U0001F1E7\U0001F1F7', 'LRD': '\U0001F1F1\U0001F1F7', 'LYD': '\U0001F1F1\U0001F1FE',
              'LSL': '\U0001F1F1\U0001F1F8', 'NAD': '\U0001F1F3\U0001F1E6', 'SZL': '\U0001F1F8\U0001F1FF',
              'ZAR': '\U0001F1FF\U0001F1E6', 'TND': '\U0001F1F9\U0001F1F3', 'MMK': '\U0001F1F2\U0001F1F2',
              'SEK': '\U0001F1F8\U0001F1EA', 'PKR': '\U0001F1F5\U0001F1F0', 'NPR': '\U0001F1F3\U0001F1F5',
              'BTN': '\U0001F1E7\U0001F1F9', 'AED': '\U0001F1E6\U0001F1EA', 'AFN': '\U0001F1E6\U0001F1EB',
              'ALL': '\U0001F1E6\U0001F1F1', 'AMD': '\U0001F1E6\U0001F1F2',
              'BDT': '\U0001F1E7\U0001F1E9', 'AWG': '\U0001F1E6\U0001F1FC', 'AZN': '\U0001F1E6\U0001F1FF',
              'BAM': '\U0001F1E7\U0001F1E6', 'BBD': '\U0001F1E7\U0001F1E7', 'BGN': '\U0001F1E7\U0001F1EC',
              'BHD': '\U0001F1E7\U0001F1ED', 'BIF': '\U0001F1E7\U0001F1EE', 'BND': '\U0001F1E7\U0001F1F3',
              'BOB': '\U0001F1E7\U0001F1F4', 'BSD': '\U0001F1E7\U0001F1F8', 'BMD': '\U0001F1E7\U0001F1F2',
              'BWP': '\U0001F1E7\U0001F1FC', 'BYR': '\U0001F1E7\U0001F1FE', 'BYN': '\U0001F1E7\U0001F1FE',
              'BZD': '\U0001F1E7\U0001F1FF', 'XAF': '\U0001F1E8\U0001F1EB', 'CDF': '\U0001F1E8\U0001F1E9',
              'CHF': '\U0001F1E8\U0001F1ED', 'CLP': '\U0001F1E8\U0001F1F1', 'CNY': '\U0001F1E8\U0001F1F3',
              'COP': '\U0001F1E8\U0001F1F4', 'CRC': '\U0001F1E8\U0001F1F7', 'CUP': '\U0001F1E8\U0001F1FA',
              'CVE': '\U0001F1E8\U0001F1FB', 'CZK': '\U0001F1E8\U0001F1FF', 'DJF': '\U0001F1E9\U0001F1EF',
              'DKK': '\U0001F1E9\U0001F1F0', 'DOP': '\U0001F1E9\U0001F1F4', 'DZD': '\U0001F1E9\U0001F1FF',
              'EGP': '\U0001F1EA\U0001F1EC', 'ERN': '\U0001F1EA\U0001F1F7', 'ETB': '\U0001F1EA\U0001F1F9',
              'FJD': '\U0001F1EB\U0001F1EF', 'FKP': '\U0001F1EB\U0001F1F0', 'GEL': '\U0001F1EC\U0001F1EA',
              'GGP': '\U0001F1EC\U0001F1EC', 'GHS': '\U0001F1EC\U0001F1ED', 'GIP': '\U0001F1EC\U0001F1EE',
              'GMD': '\U0001F1EC\U0001F1F2', 'GNF': '\U0001F1EC\U0001F1F3', 'GTQ': '\U0001F1EC\U0001F1F9',
              'GYD': '\U0001F1EC\U0001F1FE', 'HKD': '\U0001F1ED\U0001F1F0', 'HNL': '\U0001F1ED\U0001F1F3',
              'HRK': '\U0001F1ED\U0001F1F7', 'HTG': '\U0001F1ED\U0001F1F9', 'HUF': '\U0001F1ED\U0001F1FA',
              'IDR': '\U0001F1EE\U0001F1E9', 'ILS': '\U0001F1EE\U0001F1F1', 'IQD': '\U0001F1EE\U0001F1F6',
              'ISK': '\U0001F1EE\U0001F1F8', 'JMD': '\U0001F1EF\U0001F1F2', 'JOD': '\U0001F1EF\U0001F1F4',
              'KES': '\U0001F1F0\U0001F1EA', 'KGS': '\U0001F1F0\U0001F1EC', 'CNH': '\U0001F1E8\U0001F1F3',
              'KHR': '\U0001F1F0\U0001F1ED', 'KMF': '\U0001F1F0\U0001F1F2', 'KPW': '\U0001F1F0\U0001F1F5',
              'KRW': '\U0001F1F0\U0001F1F7', 'KWD': '\U0001F1F0\U0001F1FC', 'KYD': '\U0001F1F0\U0001F1FE',
              'LAK': '\U0001F1F1\U0001F1E6', 'LBP': '\U0001F1F1\U0001F1E7', 'LKR': '\U0001F1F1\U0001F1F0',
              'MAD': '\U0001F1F2\U0001F1E6', 'MDL': '\U0001F1F2\U0001F1E9', 'MGA': '\U0001F1F2\U0001F1EC',
              'MKD': '\U0001F1F2\U0001F1F0', 'MNT': '\U0001F1F2\U0001F1F3', 'MOP': '\U0001F1F2\U0001F1F4',
              'MRO': '\U0001F1F2\U0001F1F7', 'MUR': '\U0001F1F2\U0001F1FA', 'MVR': '\U0001F1F2\U0001F1FB',
              'MWK': '\U0001F1F2\U0001F1FC', 'MYR': '\U0001F1F2\U0001F1FE', 'MZN': '\U0001F1F2\U0001F1FF',
              'NGN': '\U0001F1F3\U0001F1EC', 'NIO': '\U0001F1F3\U0001F1EE', 'ANG': '\U0001F1F8\U0001F1FD',
              'NOK': '\U0001F1F3\U0001F1F4', 'NZD': '\U0001F1F3\U0001F1FF', 'OMR': '\U0001F1F4\U0001F1F2',
              'PAB': '\U0001F1F5\U0001F1E6', 'PEN': '\U0001F1F5\U0001F1EA', 'PGK': '\U0001F1F5\U0001F1EC',
              'PHP': '\U0001F1F5\U0001F1ED', 'PLN': '\U0001F1F5\U0001F1F1', 'PYG': '\U0001F1F5\U0001F1FE',
              'QAR': '\U0001F1F6\U0001F1E6', 'RON': '\U0001F1F7\U0001F1F4', 'RSD': '\U0001F1F7\U0001F1F8',
              'RWF': '\U0001F1F7\U0001F1FC', 'SAR': '\U0001F1F8\U0001F1E6', 'SBD': '\U0001F1F8\U0001F1E7',
              'SCR': '\U0001F1F8\U0001F1E8', 'SLL': '\U0001F1F8\U0001F1F1', 'SOS': '\U0001F1F8\U0001F1F4',
              'SRD': '\U0001F1F8\U0001F1F7', 'STD': '\U0001F1F8\U0001F1F9',
              'SYP': '\U0001F1F8\U0001F1FE', 'THB': '\U0001F1F9\U0001F1ED', 'TJS': '\U0001F1F9\U0001F1EF',
              'TMT': '\U0001F1F9\U0001F1F2', 'TOP': '\U0001F1F9\U0001F1F4', 'SGD': '\U0001F1F8\U0001F1EC',
              'TTD': '\U0001F1F9\U0001F1F9', 'TWD': '\U0001F1F9\U0001F1FC', 'TZS': '\U0001F1F9\U0001F1FF',
              'UAH': '\U0001F1FA\U0001F1E6', 'UGX': '\U0001F1FA\U0001F1EC', 'UYU': '\U0001F1FA\U0001F1FE',
              'UZS': '\U0001F1FA\U0001F1FF', 'VND': '\U0001F1FB\U0001F1F3', 'VUV': '\U0001F1FB\U0001F1FA',
              'WST': '\U0001F1FC\U0001F1F8', 'YER': '\U0001F1FE\U0001F1EA', 'ZMW': '\U0001F1FF\U0001F1F2',
              'EEK': '\U0001F1EA\U0001F1EA', 'IMP': '\U0001F1EE\U0001F1F2', 'SHP': '\U0001F1F8\U0001F1ED',
              'SSP': '\U0001F1F8\U0001F1F8', }


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



