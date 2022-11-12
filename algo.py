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
%matplotlib inline
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

income_statement = pd.DataFrame(get_jsonparsed_data(base_url+'income-statement/' + ticker + '?apikey=' + apiKey))
income_statement = income_statement.set_index('date')
income_statement = income_statement.apply(pd.to_numeric, errors='coerce')

income_statement.iloc[:,4:]

balance_sheet = pd.DataFrame(get_jsonparsed_data(base_url+'balance-sheet-statement/' + ticker + '?apikey=' + apiKey))
balance_sheet = balance_sheet.set_index('date')
balance_sheet = balance_sheet.apply(pd.to_numeric, errors='coerce')

balance_sheet.iloc[:,4:]

print(income_statement)
print(balance_sheet)
