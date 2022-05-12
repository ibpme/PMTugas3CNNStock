import numpy as np
import pandas as pd

def STOCH(data: pd.DataFrame, periods:int = 14):

    high_roll = data["High"].rolling(periods).max()
    low_roll = data["Low"].rolling(periods).min()
    
    # Fast stochastic indicator
    num = data["Close"] - low_roll
    denom = high_roll - low_roll
    slow_k = (num / denom) * 100
    
    # Slow stochastic indicator
    slow_d = slow_k.rolling(3).mean()
    return slow_k.values, slow_d.values
