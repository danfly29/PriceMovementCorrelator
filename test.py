import numpy as np
from pricehistory import TimeValueSeries , pd
from statisticalutils import SomethingValueStatistics

aapl = TimeValueSeries('AAPL')
aapl.read_csv_adj_close()
a= SomethingValueStatistics()
a.calc_geometricmean_return(aapl.series)

bac = TimeValueSeries('BAC')
bac.read_csv_adj_close()
b= SomethingValueStatistics()
b.calc_geometricmean_return(bac.series)
