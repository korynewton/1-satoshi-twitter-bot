# @1satoshibot
import requests
import random
import tweepy as tp
import time
from settings import *
from emoji_dict import *
import pickle


# twitter credentials
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_secret = ACCESS_SECRET
fixer_key = FIXER_KEY


class ScheduledTweet():
    def __init__(self):
        self.auth = tp.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_secret)
        self.api = tp.API(self.auth)
        self.symbol_key = ['GBP', 'JPY', 'EUR', 'USD', 'KZT', 'AUD', 'CAD', 'INR', 'RUB', 'TRY', 'VES', 'ZWL', 'MXN', 'ARS', 'AOA', 'BRL', 'ZAR', 'LRD', 'LYD', 'LSL', 'NAD', 'SZL', 'TND', 'MMK', 'SEK', 'PKR', 'NPR', 'BTN', 'AED', 'AFN', 'ALL', 'AMD', 'AOA', 'BDT', 'AWG', 'AZN', 'BAM', 'BBD', 'BGN', 'BHD', 'BIF', 'BND', 'BOB', 'BSD', 'BMD', 'BWP', 'BYN', 'BZD', 'XAF', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'FJD', 'FKP', 'GEL', 'GGP', 'GHS', 'GIP', 'GNF', 'GTQ', 'GYD',
                           'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IQD', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD', 'LAK', 'LBP', 'LKR', 'MAD', 'MDL', 'MGA', 'MKD', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RWF', 'SAR', 'SBD', 'SCR', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VND', 'VUV', 'WST', 'YER', 'ZMW', 'CUP', 'KPW', 'SYP', 'SDG', 'IRR', 'BYR', 'GMD']

        self.compose()

    def compose(self):
        pickle_in = open('price_data.txt', 'rb')
        rates_data = pickle.load(pickle_in)

        # Select currencies at random
        random_select = random.sample(self.symbol_key, 13)

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
            '            ' + '#Bitcoin #StackingSats'
        # print(to_be_tweeted)
        self.tweet(to_be_tweeted)

    def tweet(self, text):
        self.api.update_status(text)
        print('tweeted scheduled tweet')
