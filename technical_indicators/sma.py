import numpy as np
import pandas as pd

def SMA(data: pd.DataFrame, period = 14) -> np.ndarray:
    return data['Close'].rolling(period).mean().values
