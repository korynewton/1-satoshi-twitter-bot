import os
from os.path import join, dirname
from dotenv import load_dotenv
from emoji_dict import emoji_dict

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")
FIXER_KEY = os.environ.get("FIXER_KEY")
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
              'BYR', 'GMD', 'ANG', 'CNH', 'EEK', 'IMP', 'SGD', 'SHP', 'SSP',
              'VEF']


# North America currencies
NA_CURR = ['USD', 'MXN', 'CAD', 'NIO', 'JMD', 'HTG', 'HNL', 'GTQ',
           'DOP', 'CUP', 'CRC', 'KYD', 'BMD', 'BZD', 'BBD', 'BSD',
           'AWG', 'ANG', 'TTD']
# South America currencies
SA_CURR = ['ARS', 'BOB', 'BRL', 'CLP', 'COP', 'FKP', 'GYD',
           'PYG', 'PEN', 'SRD', 'UYU', 'VES', 'USD', 'EUR',
           'VEF', 'PAB']
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


# coinbase_api = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BAT', 'BBD', 'BCH', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BSV', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNH', 'CNY', 'COP', 'CRC', 'CUC', 'CVE', 'CZK', 'DAI', 'DJF', 'DKK', 'DOP', 'DZD', 'EEK', 'EGP', 'EOS', 'ERN', 'ETB', 'ETC', 'ETH', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LINK',
#                        'LKR', 'LRD', 'LSL', 'LTC', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MTL', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'REP', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'SSP', 'STD', 'SVC', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'USDC', 'UYU', 'UZS', 'VEF', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XLM', 'XOF', 'XPD', 'XPF', 'XPT', 'XRP', 'XTZ', 'YER', 'ZAR', 'ZEC', 'ZMK', 'ZMW', 'ZRX', 'ZWL']
