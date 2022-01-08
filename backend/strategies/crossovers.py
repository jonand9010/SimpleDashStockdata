import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from technical_analysis.models import MovingAverage

class MACD:

    def __init__(self, df, a = 12, b = 26, c = 9):

        self.a = a
        self.b = b
        self.c = c
        self.df = df

        self.get_macd()

        self.get_signal()
        self.divergence = self.macd - self.signal
        self.get_crossovers_idx()


    def get_macd(self):
        
        self.fast_ema = MovingAverage(self.df).EMA(halflife = self.a)

        self.slow_ema = MovingAverage(self.df).EMA(halflife = self.b)
        self.macd = self.slow_ema - self.fast_ema


    def get_signal(self):

        self.signal = MovingAverage(self.macd).EMA(halflife = self.c)

    

    def get_crossovers_idx(self):

        self.crossovers_idx = np.argwhere(np.diff(np.sign(self.macd - self.signal))).flatten()


    def plot(self):
        #sns.set_theme(style = 'darkgrid')
        #fig, ax = plt.subplots(2,1)
        #ax_twin = ax.twinx()
        fig = go.Figure(layout=go.Layout(title=go.layout.Title(text='MACD')))
        fig = make_subplots(rows=2, figure= fig )
        fig.add_trace(go.Scatter(x = self.df.index, y=self.df, mode="lines", name = 'Raw data'), row = 1, col = 1)
        fig.add_trace(go.Scatter(x = self.df.index, y=self.slow_ema, mode="lines", name = 'Slow EMA'), row = 1, col = 1)
        fig.add_trace(go.Scatter(x = self.df.index, y=self.fast_ema, mode="lines", name = 'Fast EMA'), row = 1, col = 1)

        fig.add_trace(go.Bar(x = self.df.index, y=self.divergence, name = 'Divergence'), row = 2, col = 1)
        fig.add_trace(go.Scatter(x = self.df.index, y = self.macd, mode="lines", name = 'MACD'), row = 2, col = 1)
        fig.add_trace(go.Scatter(x = self.df.index, y=self.signal, mode="lines", name = 'MACD signal'), row = 2, col = 1)
        fig.add_trace(go.Scatter(x = self.df.index[self.crossovers_idx], y=self.signal[self.crossovers_idx], name = 'trigger points',  mode = 'markers'), row = 2, col = 1)

        fig.show()


