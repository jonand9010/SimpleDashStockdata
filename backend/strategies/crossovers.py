import numpy as np
from technical_analysis.models import MovingAverage

def ma_crossover(fast_ma, slow_ma):
    

    idx = np.argwhere(np.diff(np.sign(fast_ma - slow_ma))).flatten()

    return idx