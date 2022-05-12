import numpy as np
import pandas as pd

def BBANDS(data: pd.DataFrame, period = 14, F = 2) -> tuple(np.ndarray,np.ndarray,np.ndarray):
    TP = (data['High'] + data['Low'] + data['Close'])/3
    mid = TP.rolling(period).mean()
    up = mid + F * TP.std()
    low = mid - F * TP.std()
    return mid, up, low
