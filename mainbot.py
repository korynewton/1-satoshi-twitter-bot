# @1satoshibot
import requests
import random
import tweepy as tp
import time
from settings import *


#twitter credentials
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_secret = ACCESS_SECRET

#login to twitter
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api =  tp.API(auth)

#fixer API access
main_api = 'http://data.fixer.io/api/latest'
access_key = '?access_key='
base = '&base=EUR'
symbols = '&symbols=BTC,GBP,JPY,EUR,USD,KZT,AUD,CAD,INR,RUB,TRY,VEF,ZWL,MXN,IRR,SDG,ARS,AOA,BRL,LRD,LYD,LSL,NAD,SZL,ZAR,TND,MMK,SEK,PKR,NPR,BTN,AED,AFN,,ALL,AMD,AOA,BDT,AWG,AZN,BAM,BBD,BGN,BHD,BIF,BND,BOB,BSD,BMD,BWP,BYN,BZD,XAF,CDF,CHF,CLP,CNY,COP,CRC,CUP,CVE,CZK,DJF,DKK,DOP,DZD,EGP,ERN,ETB,FJD,,FKP,GEL,GGP,GHS,GIP,GNF,GTQ,GYD,HKD,HNL,HRK,HTG,HUF,IDR,ILS,IQD,ISK,JMD,JOD,JPY,KES,KGS,KHR,KMF,KPW,KRW,KWD,KYD,LAK,LBP,LKR,MAD,MDL,MGA,MKD,MNT, ,MOP,MRO,MUR,MVR,MWK,MOP,MRO,MUR,MVR,MWK,MYR,MZN,NAD,NGN,NIO,NOK,NZD,OMR,PAB,PEN,PGK,PHP,PLN,PYG,QAR,RON,RSD,RWF,SAR,SBD,SCR,SLL,SOS,SRD,STD,SVC,SYP,THB,TJS,TMT,TND,TOP,TTD,TWD,TZS,UAH,UGX,UYU,UZS,VND,VUV,WST,YER,ZMW'

#list of symbols minus BTC that will be used as keys
symbol_key=['GBP','JPY','EUR','USD','KZT','AUD','CAD','INR','RUB','TRY','VES','ZWL','MXN','IRR','SDG','ARS','AOA','BRL','ZAR',
            'LRD','LYD','LSL','NAD','SZL','TND','MMK','SEK', 'PKR','NPR','BTN','AED','AFN','ALL','AMD','AOA','BDT','AWG','AZN','BAM','BBD',
            'BGN','BHD','BIF','BND','BOB','BSD','BMD','BWP','BYN','BZD','XAF','CDF','CHF','CLP','CNY','COP','CRC','CUP','CVE','CZK',
            'DJF','DKK','DOP','DZD','EGP','ERN','ETB','FJD','FKP','GEL','GGP','GHS','GIP','GNF','GTQ','GYD','HKD','HNL','HRK',
            'HTG','HUF','IDR','ILS','IQD','ISK','JMD','JOD','JPY','KES','KGS','KHR','KMF','KPW','KRW','KWD','KYD','LAK','LBP',
            'LKR','MAD','MDL','MGA','MKD','MNT','MOP','MRO','MUR','MVR','MWK','MYR','MZN','NAD','NGN','NIO','NOK','NZD','OMR',
            'PAB','PEN','PGK','PHP','PLN','PYG','QAR','RON','RSD','RWF','SAR','SBD','SCR','SLL','SOS','SRD','STD','SVC','SYP',
            'THB','TJS','TMT','TND','TOP','TTD','TWD','TZS','UAH','UGX','UYU','UZS','VND','VUV','WST','YER','ZMW']
#emoji dictionary with currency symbole as key and emoji code as value
emoji_dict = {'GBP':'\U0001F1EC\U0001F1E7','JPY':'\U0001F1EF\U0001F1F5',
             'EUR':'\U0001F1EA\U0001F1FA','USD':'\U0001F1FA\U0001F1F8','KZT':'\U0001F1F0\U0001F1FF',
             'AUD':'\U0001F1E6\U0001F1FA','CAD':'\U0001F1E8\U0001F1E6','INR':'\U0001F1EE\U0001F1F7',
             'RUB':'\U0001F1F7\U0001F1FA','TRY':'\U0001F1F9\U0001F1F7','VES':'\U0001F1FB\U0001F1EA',
             'ZWL':'\U0001F1FF\U0001F1FC','MXN':'\U0001F1F2\U0001F1FD','IRR':'\U0001F1EE\U0001F1F7',
             'SDG':'\U0001F1F8\U0001F1E9','ARS':'\U0001F1E6\U0001F1F7','AOA':'\U0001F1E6\U0001F1F4',
             'BRL':'\U0001F1E7\U0001F1F7','LRD':'\U0001F1F1\U0001F1F7','LYD':'\U0001F1F1\U0001F1FE',
             'LSL':'\U0001F1F1\U0001F1F8','NAD':'\U0001F1F3\U0001F1E6','SZL':'\U0001F1F8\U0001F1FF',
             'ZAR':'\U0001F1FF\U0001F1E6','TND':'\U0001F1F9\U0001F1F3','MMK':'\U0001F1F2\U0001F1F2',
              'SEK':'\U0001F1F8\U0001F1EA','PKR':'\U0001F1F5\U0001F1F0','NPR':'\U0001F1F3\U0001F1F5',
              'BTN':'\U0001F1E7\U0001F1F9','AED':'\U0001F1E6\U0001F1EA','AFN':'\U0001F1E6\U0001F1EB',
              'ALL':'\U0001F1E6\U0001F1F1','AMD':'\U0001F1E6\U0001F1F2','AOA':'\U0001F1E6\U0001F1F4',
              'BDT':'\U0001F1E7\U0001F1E9','AWG':'\U0001F1E6\U0001F1FC','AZN':'\U0001F1E6\U0001F1FF',
              'BAM':'\U0001F1E7\U0001F1E6','BBD':'\U0001F1E7\U0001F1E7','BGN':'\U0001F1E7\U0001F1EC',
              'BHD':'\U0001F1E7\U0001F1ED','BIF':'\U0001F1E7\U0001F1EE','BND':'\U0001F1E7\U0001F1F3',
              'BOB':'\U0001F1E7\U0001F1F4','BSD':'\U0001F1E7\U0001F1F8','BMD':'\U0001F1E7\U0001F1F2',
              'BWP':'\U0001F1E7\U0001F1FC','BYR':'\U0001F1E7\U0001F1FE','BYN':'\U0001F1E7\U0001F1FE',
              'BZD':'\U0001F1E7\U0001F1FF','XAF':'\U0001F1E8\U0001F1EB','CDF':'\U0001F1E8\U0001F1E9',
              'CHF':'\U0001F1E8\U0001F1ED','CLP':'\U0001F1E8\U0001F1F1','CNY':'\U0001F1E8\U0001F1F3',
              'COP':'\U0001F1E8\U0001F1F4','CRC':'\U0001F1E8\U0001F1F7','CUP':'\U0001F1E8\U0001F1FA',
              'CVE':'\U0001F1E8\U0001F1FB','CZK':'\U0001F1E8\U0001F1FF','DJF':'\U0001F1E9\U0001F1EF',
              'DKK':'\U0001F1E9\U0001F1F0','DOP':'\U0001F1E9\U0001F1F4','DZD':'\U0001F1E9\U0001F1FF',
              'EGP':'\U0001F1EA\U0001F1EC','ERN':'\U0001F1EA\U0001F1F7','ETB':'\U0001F1EA\U0001F1F9',
              'FJD':'\U0001F1EB\U0001F1EF','FKP':'\U0001F1EB\U0001F1F0','GEL':'\U0001F1EC\U0001F1EA',
              'GGP':'\U0001F1EC\U0001F1EC','GHS':'\U0001F1EC\U0001F1ED','GIP':'\U0001F1EC\U0001F1EE',
              'GMD':'\U0001F1EC\U0001F1F2','GNF':'\U0001F1EC\U0001F1F3','GTQ':'\U0001F1EC\U0001F1F9',
              'GYD':'\U0001F1EC\U0001F1FE','HKD':'\U0001F1ED\U0001F1F0','HNL':'\U0001F1ED\U0001F1F3',
              'HRK':'\U0001F1ED\U0001F1F7','HTG':'\U0001F1ED\U0001F1F9','HUF':'\U0001F1ED\U0001F1FA',
              'IDR':'\U0001F1EE\U0001F1E9','ILS':'\U0001F1EE\U0001F1F1','IQD':'\U0001F1EE\U0001F1F6',
              'ISK':'\U0001F1EE\U0001F1F8','JMD':'\U0001F1EF\U0001F1F2','JOD':'\U0001F1EF\U0001F1F4',
              'JPY':'\U0001F1EF\U0001F1F5','KES':'\U0001F1F0\U0001F1EA','KGS':'\U0001F1F0\U0001F1EC',
              'KHR':'\U0001F1F0\U0001F1ED','KMF':'\U0001F1F0\U0001F1F2','KPW':'\U0001F1F0\U0001F1F5',
              'KRW':'\U0001F1F0\U0001F1F7','KWD':'\U0001F1F0\U0001F1FC','KYD':'\U0001F1F0\U0001F1FE',
              'LAK':'\U0001F1F1\U0001F1E6','LBP':'\U0001F1F1\U0001F1E7','LKR':'\U0001F1F1\U0001F1F0',
              'MAD':'\U0001F1F2\U0001F1E6','MDL':'\U0001F1F2\U0001F1E9','MGA':'\U0001F1F2\U0001F1EC',
              'MKD':'\U0001F1F2\U0001F1F0','MNT':'\U0001F1F2\U0001F1F3','MOP':'\U0001F1F2\U0001F1F4',
              'MRO':'\U0001F1F2\U0001F1F7','MUR':'\U0001F1F2\U0001F1FA','MVR':'\U0001F1F2\U0001F1FB',
              'MWK':'\U0001F1F2\U0001F1FC','MYR':'\U0001F1F2\U0001F1FE','MZN':'\U0001F1F2\U0001F1FF',
              'NAD':'\U0001F1F3\U0001F1E6','NGN':'\U0001F1F3\U0001F1EC','NIO':'\U0001F1F3\U0001F1EE',
              'NOK':'\U0001F1F3\U0001F1F4','NZD':'\U0001F1F3\U0001F1FF','OMR':'\U0001F1F4\U0001F1F2',
              'PAB':'\U0001F1F5\U0001F1E6','PEN':'\U0001F1F5\U0001F1EA','PGK':'\U0001F1F5\U0001F1EC',
              'PHP':'\U0001F1F5\U0001F1ED','PLN':'\U0001F1F5\U0001F1F1','PYG':'\U0001F1F5\U0001F1FE',
              'QAR':'\U0001F1F6\U0001F1E6','RON':'\U0001F1F7\U0001F1F4','RSD':'\U0001F1F7\U0001F1F8',
              'RWF':'\U0001F1F7\U0001F1FC','SAR':'\U0001F1F8\U0001F1E6','SBD':'\U0001F1F8\U0001F1E7',
              'SCR':'\U0001F1F8\U0001F1E8','SLL':'\U0001F1F8\U0001F1F1','SOS':'\U0001F1F8\U0001F1F4',
	      'SRD':'\U0001F1F8\U0001F1F7','STD':'\U0001F1F8\U0001F1F9','SVC':'\U0001F1F8\U0001F1FB',
              'SYP':'\U0001F1F8\U0001F1FE','THB':'\U0001F1F9\U0001F1ED','TJS':'\U0001F1F9\U0001F1EF',
              'TMT':'\U0001F1F9\U0001F1F2','TND':'\U0001F1F9\U0001F1F3','TOP':'\U0001F1F9\U0001F1F4',
              'TTD':'\U0001F1F9\U0001F1F9','TWD':'\U0001F1F9\U0001F1FC','TZS':'\U0001F1F9\U0001F1FF',
              'UAH':'\U0001F1FA\U0001F1E6','UGX':'\U0001F1FA\U0001F1EC','UYU':'\U0001F1FA\U0001F1FE',
              'UZS':'\U0001F1FA\U0001F1FF','VND':'\U0001F1FB\U0001F1F3','VUV':'\U0001F1FB\U0001F1FA',
              'WST':'\U0001F1FC\U0001F1F8','YER':'\U0001F1FE\U0001F1EA','ZMW':'\U0001F1FF\U0001F1F2'}

#global variables
to_be_tweeted = ''
rates_data = {}
random_select = {}


# grab fixer.io price data, convert it to pps and pick 12 symbols at random
rates_data = {}
def fixer():
    global rates_data
    global random_select
    url = main_api + access_key + base + symbols
    json_data = requests.get(url).json()
    rates_data = dict.items(json_data['rates'])
    rates_data = dict(rates_data)
    EUR = rates_data['EUR']
    BIT = rates_data['BTC']
    bitprice = (EUR / BIT)
    rates_data.update((x,y*bitprice / 100000000) for x, y in rates_data.items())
    rates_data['VEF'] /= 100000
    rates_data['VES'] = rates_data.pop('VEF')
    random_select = random.sample(symbol_key,12)
    compose()

#compose 2 column tweet
def compose():
    global to_be_tweeted
    for i in range(len(random_select)):
        key = random_select[i]
        emoji = emoji_dict[key]
        price = '{0:.5f}'.format(rates_data[key])
        if i % 2 == 0:
            even_line = '\n' + emoji + ': ' + str(price) + ' ' + key
            to_be_tweeted = to_be_tweeted + even_line
        else:
            odd_line = '   ' + emoji + ': ' + str(price) + ' ' + key
            to_be_tweeted = to_be_tweeted + odd_line
        i += 1
    to_be_tweeted = to_be_tweeted + '\n'+ '                       #Bitcoin'
    tweet()

# tweet function
def tweet():
    global to_be_tweeted
    global rates_data
    global random_select
    api.update_status(to_be_tweeted)
    print(random_select)
    print('tweeted')
    to_be_tweeted = ''
    rates_data = {}
    random_select = []
    time.sleep(5400)
    fixer()

fixer()
