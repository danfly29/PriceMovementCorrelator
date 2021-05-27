class PriceHistoryScrapper:
    import csv
    import urllib.request, urllib.parse, urllib.error
    import ssl #foe error handling

    def accept_symbol(self,listy):
        #Ignores certificates errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE



        if listy:
            #Create list of stocks using the contents of list of stocks file
            fhand = open('list_of_stocks.txt')
            stocks = []
            for stock in fhand:
                stocks.append(stock.strip())


            for stock_ticker in stocks:
                url = 'https://query1.finance.yahoo.com/v7/finance/download/'+stock_ticker+'?period1=1463097600&period2=1620864000&interval=1d&events=history&includeAdjustedClose=true'
                html = urllib.request.urlopen(url, context=ctx).read()
                fhand = open(stock_ticker+'.csv','wb')
                fhand.write(html)
                fhand.close()
        else:
            self.names = []
            while True:
                self.name =input('What is the symbol we will scrape')
                url = 'https://query1.finance.yahoo.com/v7/finance/download/'+self.name+'?period1=1463097600&period2=1620864000&interval=1d&events=history&includeAdjustedClose=true'
                html = urllib.request.urlopen(url, context=ctx).read()
                fhand = open(self.name+'.csv','wb')
                fhand.write(html)
                fhand.close()
                self.cont= (input('Do you have more?(y/n)')).upper()
                if self.cont=='N':
                    break

import csv
import urllib.request, urllib.parse, urllib.error
import ssl #foe error handling

listy=False
p = PriceHistoryScrapper()
p.accept_symbol(listy)
