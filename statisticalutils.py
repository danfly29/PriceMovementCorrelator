import pandas as pd

class SomethingValueStatistics:
    """Class for intro to executive finance - risk and return math"""

    def __init__(self,name=None,weight=1.0,returnseries=None,geometric_mean_return=None):
        """Initialize name and weight of a stock or portfolio"""
        self.weight=weight
        self.name=name
        self.returnseries = returnseries
        self.geometric_mean_return = geometric_mean_return

    def set_weight(self, weight):
        """Just replaces the weight attribute with watever integer or float
        parameter is passed"""
        self.weight=weight
        self.w_returnseries = self.returnseries*self.weight
        self.w_geometric_mean_return = self.geometric_mean_return*self.weight

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

    def calc_geometricmean_return(self,series,seriesr=False):
        """Uses return series to get geometric mean of returns """
        self.get_return_series(series)
        prod = self.returnseries.prod()
        size=len(self.returnseries)
        self.geometric_mean_return=prod**(1/size)


    def combine(self,othersvs,own_weight=.5,other_weight=.5):
        """Creates weighted svs objects series and"""
        self.set_weight(own_weight)
        othersvs.set_weight(other_weight)
        #self.name=self.name+othersvs.name
        return SomethingValueStatistics(geometric_mean_return=self.w_geometric_mean_return+othersvs.w_geometric_mean_return,
        returnseries = self.w_returnseries+othersvs.w_returnseries)
