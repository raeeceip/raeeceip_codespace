import json
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np


# Settings to produce nice plots in a Jupyter notebook
plt.style.use('fivethirtyeight')
# %matplotlib inline
plt.rcParams['figure.figsize'] = [12, 6]

# To extract and parse fundamental data from finviz website

# For parsing financial statements data from financialmodelingprep api


def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


# Financialmodelingprep api url
base_url = "https://financialmodelingprep.com/api/v3/"
apiKey = "177c05a372a4adb032ba8980798f042b"
ticker = 'AAPL'
# get list of stocks from financial model prep api
def get_fmp_stock_list():
    url = base_url + "stock/list?apikey=" + apiKey
    data = get_jsonparsed_data(url)
   #return top 20
def get_fmp_top20():
    url = base_url + "stock/list?apikey=" + apiKey
    data = get_jsonparsed_data(url)
    return data[0:20]
    
print (get_fmp_top20())
# get company rating from financial model prep api
def get_fmp_rating(ticker):
    url = base_url + "rating/" + ticker + "?apikey=" + apiKey
    data = get_jsonparsed_data(url)
    return data[0]['ratingScore']

# get company profile from financial model prep api
def get_fmp_profile(ticker):
# company profile contains company description, sector, industry, address, full time employees, symbol, company name, exchange, market capitalization, website, logo, phone, ceo, tagline, similar companies, etc.
    url = base_url + "profile/" + ticker + "?apikey=" + apiKey
    data = get_jsonparsed_data(url)
    return data[0]


print(get_fmp_rating(ticker))
print(get_fmp_profile(ticker))



