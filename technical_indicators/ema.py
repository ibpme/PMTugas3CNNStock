import numpy as np
import pandas as pd

def print_pretty(array):
    print('[')
    for i in array:
        print('   ', (str(i) if not np.isnan(i) else 'np.nan') + ',')
    print(']')

def EMA(data: pd.DataFrame, period:int = 10) -> np.ndarray:
    ema = data['Close'].ewm(span=period).mean()
    return ema