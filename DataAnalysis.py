#Running Python 3.6.9
# ALTGA3K77UQA49VX -- AlphaVantage key
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import datetime
import os
#!pip install alpha_vantage
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
#!pip install yfinance
import yfinance as yf


#Alpha Vantage code starts here

from alpha_vantage.timeseries import TimeSeries

'''
This method fetch real-time and historical stock prices for an equity from AlphaVantage API.
Return daily split/dividend-adjusted close for the equity from from Nov 1st, 2019 until now.
Keyword Arguments:
    symbol: the symbol for the equity we want to get its data
'''
def get_from_alpha_vantage(company_symbol:str):
    # fetch historical stock prices from AlphaVantage
    # outputsize='full' returns the full-length daily times series, commonly above 1MB
    ts = TimeSeries(key='ALTGA3K77UQA49VX', output_format='pandas', indexing_type='date')
    data, meta_data = ts.get_daily_adjusted(symbol=company_symbol, outputsize='full')

    # select data from Nov 1st, 2019 until now
    start_date = datetime.datetime(2019, 11, 1)
    filtered_data = data.loc[data.index.values > np.datetime64(start_date)]
    
    # only select adjusted close from given attributes
    filtered_data = filtered_data[['5. adjusted close']]
    filtered_data.columns = ['adj_close']

    return filtered_data

get_from_alpha_vantage('GOOGL')


#yfinance code starts here
from pandas_datareader import data as pandas_datareader
#nasdaq = yf.Ticker("^IXIC")
#print(nasdaq.info)
#hist =nasdaq.history(period="1y")
#print(hist)
yf.pdr_override
df = pdr.get_data_yahoo("000001.SS", start = "2019-01-01", end = "2020-07-01")
#df.head()
new_df = pd.DataFrame(df,columns=["Close"])
print(new_df)
new_df.to_csv("sse.csv")

# Scraping index data from various countries and saving it in their specific variable names
# S&P500
USA_SP500 = yf.Ticker("^GSPC").history(period="1y")
USA_SP500

# NASDAQ
USA_NAS = yf.Ticker("^IXIC").history(period="1y")
USA_NAS

# DOW JONES
USA_DJ = yf.Ticker("DJI").history(period="1y")
USA_DJ

# NIKKEI 225
nikkei = yf.Ticker("^N225").history(period="1y")
nikkei

# FTSE 100
ftse = yf.Ticker("^FTSE").history(period="1y")
ftse = ftse[['Close']]
ftse