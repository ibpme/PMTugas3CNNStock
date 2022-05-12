import numpy as np
import pandas as pd

def AROON(data: pd.DataFrame, lb = 25) -> np.ndarray:
    up = 100 * data['High'].rolling(lb + 1).apply(lambda x: x.argmax()) / lb
    down = 100 * data['Low'].rolling(lb + 1).apply(lambda x: x.argmin()) / lb

    return up, down
