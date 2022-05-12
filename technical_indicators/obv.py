import numpy as np
import pandas as pd

def OBV(data: pd.DataFrame) -> np.ndarray:
    current_obv = 0
    obv = [current_obv]
    for i in range(1,len(data)):
        if data["Close"][i] > data["Close"][i-1]:
            current_obv = obv[i-1] + data["Volume"][i]
        elif data["Close"][i] < data["Close"][i-1]:
            current_obv = obv[i-1] - data["Volume"][i]
        else:
            current_obv = obv[i-1]
        obv.append(current_obv)

    return np.array(obv)

if __name__ == "__main__":
    data = pd.read_csv("../data/data.csv")
    print(data[["Close","Volume"]])
    obv_arr = OBV(data)
    print(len(obv_arr))
    print(obv_arr)
