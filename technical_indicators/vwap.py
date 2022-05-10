import numpy as np
import pandas as pd


def VWAP(data: pd.DataFrame) -> np.ndarray:
    pv = (data["High"].values +
          data["Low"].values + data["Close"].values)/3
    volume = data["Volume"].values
    vwap_arr = []
    for i in range(1, len(data)):
        cum_vol = sum(volume[:i])
        vwap = (pv[i]*volume[i])/cum_vol
        vwap_arr.append(vwap)

    return np.array(vwap_arr)


if __name__ == "__main__":
    data = pd.read_csv("../data/data.csv")
    print(VWAP(data))
