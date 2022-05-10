import numpy as np
import pandas as pd


def RSI(data: pd.DataFrame) -> np.ndarray:
    up_avg = 0
    dn_avg = 0
    n = len(data)
    for i in range(1, n):
        prev_close = data["Close"][i-1]
        close = data["Close"][i]
        if close > prev_close:
            up = close - prev_close
            dn = 0
        else:
            up = 0
            dn = prev_close - close
        up_avg = (up_avg*(n-1) + up)/n
        dn_avg = (dn_avg*(n-1) + dn)/n

    rmi = 100*up_avg/(up_avg+dn_avg)

    return np.array(rmi)


if __name__ == "__main__":
    data = pd.read_csv("../data/data.csv")
    print(RSI(data))
