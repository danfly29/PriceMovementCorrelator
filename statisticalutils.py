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
        copy = copy.drop([0]).set_index(['Date']).reset_index()
        df['Numerator']=copy['Numerator']
        df["% Change"]=df['Numerator']/df['Adj Close']
