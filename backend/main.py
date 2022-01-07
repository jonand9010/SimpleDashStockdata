from data.scrape import get_yahoo_finance_data
import pandas as pd
import matplotlib.pyplot as plt
from analysis.models import MovingAverage
df = get_yahoo_finance_data('KINV-B.ST')
moving_average = MovingAverage()

moving_average.SMA(df['Open'], 50)
test = df['Open'].rolling(50, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None).mean()

plt.plot(df['Open'])
plt.plot(moving_average.sma)

plt.show()