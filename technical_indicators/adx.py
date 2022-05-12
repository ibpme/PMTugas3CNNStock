import numpy as np
import pandas as pd


def DI(data: pd.DataFrame) -> tuple:
    plusdm_sum = 0
    minusdm_sum = 0
    n = len(data)
    true_range_sum = 0
    for i in range(1, n):
        delta_high = data["High"][i-1] - data["High"][i]
        delta_low = data["Low"][i] - data["Low"][i-1]

        if (delta_high < 0 and delta_low < 0) or delta_high == delta_low:
            plusdm = 0
            minusdm = 0
        elif (delta_high > delta_low):
            plusdm = delta_high
            minusdm = 0
        elif (delta_high < delta_low):
            plusdm = 0
            minusdm = delta_low
        plusdm_sum = plusdm_sum - plusdm_sum/n + plusdm
        minusdm_sum = minusdm_sum - minusdm_sum/n + minusdm
        # Modified for non intra day data
        true_high = max(data["High"][i], data["Close"][i-1])
        true_low = min(data["High"][i], data["Close"][i-1])

        true_range = true_high - true_low
        true_range_sum = true_range_sum - true_range_sum/n + true_range

    plusdi = 100*plusdm_sum/true_range_sum
    minusdi = 100*minusdm_sum/true_range_sum

    return plusdi, minusdi


def DX(data: pd.DataFrame) -> np.ndarray:
    plusdi, minusdi = DI(data)
    dx = (plusdi - minusdi)/(plusdi+minusdi)
    return dx


def ADX(data: pd.DataFrame) -> np.ndarray:
    dx = DX(data)
    adx = 0
    n = len(data)
    for i in range(n):
        adx = (adx*(n-1) + dx)/n
    return np.array(adx)


if __name__ == "__main__":
    data = pd.read_csv("../data/data.csv")
    print(ADX(data))
