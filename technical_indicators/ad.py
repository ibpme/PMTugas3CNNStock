import numpy as np
import pandas as pd


def AD(data: pd.DataFrame) -> np.ndarray:
    ad = 0
    close = data["Close"].values
    low = data["Low"].values
    high = data["High"].values
    volume = data["Volume"].values
    clv = (2*close - low - high)/(high-low + 1e-5)
    for vol in volume:
        ad += clv*vol
    return np.array(ad)


if __name__ == "__main__":
    data = pd.read_csv("../data/data.csv")
    print(AD(data))
