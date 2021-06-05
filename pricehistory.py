class TimeValueSeries:
    '''Class for Adj. Close Price by Date for a Stock or Portfolio'''
    def __init__(self,name,series=None, weight=1):
        '''Initialize the name and weight(in context of a Portfolio, default is 1) of a new TimeValueSeries'''
        self.name=name
        self.series=series
    def read_series_from_csv(self):
        import pandas as pd
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
