import numpy as np
import pandas as pd


def ROC(data: pd.DataFrame, p=3) -> np.ndarray:
    roc_arr = []
    for i in range(p, len(data), p):
        roc = 100*(data["Close"][i]-data["Close"][i-p])/data["Close"][i-p]
        roc_arr.append(roc)
    return np.array(roc_arr)


if __name__ == "__main__":
    data = pd.read_csv("../data/data.csv")
    print(ROC(data))
