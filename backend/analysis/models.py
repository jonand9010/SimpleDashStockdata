import pandas as pd

class MovingAverage:
    def __init__(self):
        pass

    def SMA(self, df, window, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None):
        "Simple moving average"
        
        self.sma = df.rolling(window, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None).mean()


    def EMA(self, df, com=None, span=None, halflife=None, alpha=None, min_periods=0, adjust=True, ignore_na=False, axis=0, times=None):
        "Exponential weighted moving average"

        self.ema = df.ewm(com=None, span=None, halflife=None, alpha=None, min_periods=0, adjust=True, ignore_na=False, axis=0, times=None)

    def CMA(self, df, min_periods=1, center=None, axis=0, method='single'):
        "Cumulative moving average"

        self.cma = df.expanding(min_periods=1, center=None, axis=0, method='single')