# GetStockQuote.py
# Get Current Stock
# 2-15-2017
#
import requests
stock = input('Enter Stock Symbol: ')
ss = "http://download.finance.yahoo.com/d/quotes.csv?s=" + stock + "&f=l1"
r = requests.get(ss)
print('Current: ', stock, r.text)
