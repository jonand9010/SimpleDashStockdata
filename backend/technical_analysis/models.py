import pandas as pd

class MovingAverage:
    def __init__(self, df, window):
        self.df = df
        self.window = window
        

    def SMA(self, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None):
        "Simple moving average"

        self.sma = self.df.rolling(self.window, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None).mean()


    def EMA(self, com=None, span=None, halflife=None, alpha=None, min_periods=0, adjust=True, ignore_na=False, axis=0, times=None):
        "Exponential weighted moving average"

        self.ema = self.df.ewm(com=None, span=None, halflife=None, alpha=None, min_periods=0, adjust=True, ignore_na=False, axis=0, times=None)

    def CMA(self, min_periods=1, center=None, axis=0, method='single'):
        "Cumulative moving average"

        self.cma = self.df.expanding(min_periods=1, center=None, axis=0, method='single')