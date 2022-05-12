import numpy as np
import pandas as pd

def BBANDS(data: pd.DataFrame, period = 14, F = 2):
    TP = (data['High'] + data['Low'] + data['Close'])/3
    mid = TP.rolling(period).mean()
    up = mid + F * TP.std()
    low = mid - F * TP.std()
    return mid.values, up.values, low.values
