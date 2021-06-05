class TimeValueSeries:
    '''Class for Adj. Close Price by Date for a Stock or Portfolio'''
    def __init__(self,name,series=None, weight=1):
        '''Initialize the name and weight(in context of a Portfolio, default is 1) of a new TimeValueSeries'''
        self.name=name
        self.series=series
    def read_series_from_csv(self):
        """Method reads series from collected/csv"""
        series = pd.read_csv('collected/'+self.name+'.csv')
        self.series = series.set_index('Date').drop(['Open','High','Low','Volume','Close'],axis=1)

    def scrape_series_from_yahoo(self):
        '''Method scrapes into csv file Price History from Yahoo Finance defaults dates are bussines days from
        May 13, 2016 to May 12, 2021. Prices are Adjuste Close.'''
        #Ignores certificates errors
        url = 'https://query1.finance.yahoo.com/v7/finance/download/'+self.name+'?period1=1463097600&period2=1620864000&interval=1d&events=history&includeAdjustedClose=true'
        html = urllib.request.urlopen(url, context=ctx).read()
        fhand = open('collected/'+self.name+'.csv','wb')
        fhand.write(html)
        fhand.close()
        self.get_series_from_csv()

class SomethingValueStatistics:
    """Class for intro to executive finance - risk and return math"""

    def __init__(self,name=None,weight=1):
        """Initialize name and weight of a stock or portfolio"""
        self.weight=weight
        self.name=name
    def calc_expected_return(self,series):
        df = pd.DataFrame(series).reset_index()
        copy = df
        copy['Numerator'] =copy['Adj Close']
        copy = copy.drop([0])
        df['Numerator']=copy['Numerator']
        df["% Change"]=df['Numerator']/df['Adj Close']
        self.df = df.reset_index
        self.get_series_from_csv()

class SomethingValueStatistics:
    """Class for intro to executive finance - risk and return math"""

    def __init__(self,name=None,weight=1):
        """Initialize name and weight of a stock or portfolio"""
        self.weight=weight
        self.name=name
    def get_return_series(self,series):
        """Takes a Date Price Series and uses two mostly identical data frames
        two move indexes around placing today and next day prices side by side.
        Finally creating a series attribute."""
        df = pd.DataFrame(series).reset_index()
        copy = df
        copy['Numerator'] =copy['Adj Close']
        copy = copy.drop([0])
        copy = copy.set_index('Date').reset_index()
        df['Numerator']=copy['Numerator']
        copy["% Change"]=df['Numerator']/df['Adj Close']
        self.returnseries = copy.set_index('Date')['% Change']

    def calc_observed_return(self,series):
        """Uses return series to get geometric mean of returns"""
        self.get_return_series(series)
        prod = self.returnseries.prod()
        size=len(self.returnseries)
        geometric_mean_return=prod**(1/size)
        return(geometric_mean_return)



import csv
import urllib.request, urllib.parse, urllib.error
import math


import csv
import urllib.request, urllib.parse, urllib.error
import ssl #for error handling
import pandas as pd
import numpy as np

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
vz = TimeValueSeries(name='VZ')
vzstats = SomethingValueStatistics()
