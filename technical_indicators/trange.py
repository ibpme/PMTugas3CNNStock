import numpy as np
import pandas as pd

def TRANGE(data: pd.DataFrame) -> np.ndarray:
    """
    TRANGE merupakan perhitungan yang digunakan untuk
    menghitung range harga normal dari suatu nilai.
    """
    a = data['High'] - data['Low']
    b = data['High'] - data['Close'].shift(1)
    c = data['Low'] - data['Close'].shift(1)
    result =  pd.DataFrame({'a':a,'b':b,'c':c}).max(axis = 1).values

    return result
