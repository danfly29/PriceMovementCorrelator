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
