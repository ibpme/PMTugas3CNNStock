import numpy as np
import pandas as pd


def EMA(data: pd.DataFrame, period:int = 10) -> np.ndarray:
    ema = data['Close'].ewm(span=period).mean()
    return ema.values