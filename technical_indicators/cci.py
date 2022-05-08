import numpy as np
import pandas as pd

def CCI(data: pd.DataFrame, time_period:int =10) -> np.ndarray:
    """
    CCI di-design untuk mendeteksi awal dan akhir dari trend market
    Range normal dari CCI adalah 100 sampai -100. Ketika nilai CCI
    diluar itu, terindikasi oversold atau overbought

    \begin{equation}
    CCI = \frac{TP-ATP}{0.015 \times MD}

    TP = \frac{high + low + close}{3}
    ATP = \text{SimpleMovingAverage(TP)}
    MD = \text{MeanAbsolutDeviation(TP)}
    \end{equation}
    """
    tp = (data['High'] + data['Low'] + data['Close']) / 3 
    atp = tp.rolling(time_period).mean()
    md = tp.rolling(time_period).apply(lambda x: pd.Series(x).mad())
    cci = (tp - atp) / (0.015 * md)
    return cci
