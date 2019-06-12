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

# fixer API access
main_api = 'http://data.fixer.io/api/latest'
access_key = '?access_key=' + fixer_key
base = '&base=EUR'
symbols = '&symbols=BTC,GBP,JPY,EUR,USD,KZT,AUD,CAD,INR,RUB,TRY,VEF,ZWL,MXN,IRR,SDG,ARS,AOA,BRL,LRD,LYD,LSL,NAD,SZL,ZAR,TND,MMK,SEK,PKR,NPR,BTN,AED,AFN,ALL,AMD,AOA,BDT,AWG,AZN,BAM,BBD,BGN,BHD,BIF,BND,BOB,BSD,BMD,BWP,BYN,BZD,XAF,CDF,CHF,CLP,CNY,COP,CRC,CUP,CVE,CZK,DJF,DKK,DOP,DZD,EGP,ERN,ETB,FJD,FKP,GEL,GGP,GHS,GIP,GNF,GTQ,GYD,HKD,HNL,HRK,HTG,HUF,IDR,ILS,IQD,ISK,JMD,JOD,JPY,KES,KGS,KHR,KMF,KPW,KRW,KWD,KYD,LAK,LBP,LKR,MAD,MDL,MGA,MKD,MNT,MOP,MRO,MUR,MVR,MWK,MOP,MRO,MUR,MVR,MWK,MYR,MZN,NAD,NGN,NIO,NOK,NZD,OMR,PAB,PEN,PGK,PHP,PLN,PYG,QAR,RON,RSD,RWF,SAR,SBD,SCR,SLL,SOS,SRD,STD,SVC,SYP,THB,TJS,TMT,TND,TOP,TTD,TWD,TZS,UAH,UGX,UYU,UZS,VND,VUV,WST,YER,ZMW'

# list of symbols minus BTC that will be used as keys
symbol_key = ['GBP', 'JPY', 'EUR', 'USD', 'KZT', 'AUD', 'CAD', 'INR', 'RUB', 'TRY', 'VES', 'ZWL', 'MXN', 'IRR', 'SDG', 'ARS', 'AOA', 'BRL', 'ZAR',
              'LRD', 'LYD', 'LSL', 'NAD', 'SZL', 'TND', 'MMK', 'SEK', 'PKR', 'NPR', 'BTN', 'AED', 'AFN', 'ALL', 'AMD', 'AOA', 'BDT', 'AWG', 'AZN', 'BAM', 'BBD',
              'BGN', 'BHD', 'BIF', 'BND', 'BOB', 'BSD', 'BMD', 'BWP', 'BYN', 'BZD', 'XAF', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK',
              'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'FJD', 'FKP', 'GEL', 'GGP', 'GHS', 'GIP', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK',
              'HTG', 'HUF', 'IDR', 'ILS', 'IQD', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'LAK', 'LBP',
              'LKR', 'MAD', 'MDL', 'MGA', 'MKD', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NZD', 'OMR',
              'PAB', 'PEN', 'PGK', 'PHP', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RWF', 'SAR', 'SBD', 'SCR', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP',
              'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VND', 'VUV', 'WST', 'YER', 'ZMW']


#global variables
to_be_tweeted = ''
rates_data = {}
random_select = {}


# grab fixer.io price data, convert it to pps and pick 12 symbols at random
rates_data = {}


# def fixer():
#     global rates_data
#     global random_select
#     url = main_api + access_key + base + symbols
#     json_data = requests.get(url).json()
#     rates_data = dict.items(json_data['rates'])
#     rates_data = dict(rates_data)
#     EUR = rates_data['EUR']
#     BIT = rates_data['BTC']
#     bitprice = (EUR / BIT)
#     rates_data.update((x, y*bitprice / 100000000)
#                       for x, y in rates_data.items())
#     rates_data['VEF'] /= 100000
#     rates_data['VES'] = rates_data.pop('VEF')
#     random_select = random.sample(symbol_key, 12)
#     compose()

def getData():
    global random_select
    url = 'https://api.coinbase.com/v2/exchange-rates?currency=BTC'
    try:
        json_data = requests.get(url).json()['data']['rates']

        for key in emoji_dict:
            if key in json_data:
                price_sats = float(json_data[key])
                rates_data[key] = str(price_sats / 100000000)
    except:
        print('request failed')

    # for key in rates_data:
    #     rates_data[key] = str(rates_data[key])

    print(rates_data)


getData()

# compose 2 column tweet


# def compose():
#     global to_be_tweeted
#     for i in range(len(random_select)):
#         key = random_select[i]
#         emoji = emoji_dict[key]
#         price = '{0:.5f}'.format(rates_data[key])
#         if i % 2 == 0:
#             even_line = '\n' + emoji + ': ' + str(price) + ' ' + key
#             to_be_tweeted = to_be_tweeted + even_line
#         else:
#             odd_line = '   ' + emoji + ': ' + str(price) + ' ' + key
#             to_be_tweeted = to_be_tweeted + odd_line
#         i += 1
#     to_be_tweeted = to_be_tweeted + '\n' + '                       #Bitcoin'
#     tweet()

# # tweet function


# def tweet():
#     global to_be_tweeted
#     global rates_data
#     global random_select
#     api.update_status(to_be_tweeted)
#     print(random_select)
#     print('tweeted')
#     to_be_tweeted = ''
#     rates_data = {}
#     random_select = []
#     time.sleep(5400)
#     fixer()


# fixer()
