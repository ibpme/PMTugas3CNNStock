import numpy as np
import pandas as pd


def MACD(data: pd.DataFrame) -> np.ndarray:
    shortema = data["Close"][0]
    longema = data["Close"][0]
    for i in range(1, len(data)):
        price = data["Close"][i]
        shortema = 0.15*price + 0.85*shortema
        longema = 0.075*price + 0.925*longema
    macd = shortema - longema

    return np.array(macd)


if __name__ == "__main__":
    data = pd.read_csv("../data/data.csv")
    print(MACD(data))
