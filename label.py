import numpy as np
import pandas as pd

def LABEL(data: pd.DataFrame, window = 15) -> np.ndarray:
    max_window = data['Close'].rolling(window).max()
    min_window = data['Close'].rolling(window).min()
    
    is_sell = data['Close'] == max_window
    is_buy = data['Close'] == min_window
    label = np.zeros_like(data['Close'])
    for i, (b, s) in enumerate(zip(is_buy, is_sell)):
        if b:
            label[i] = 1
        elif s:
            label[i] = 2
    return label

if __name__ == "__main__":
    data = pd.read_csv("./data/data.csv")
    print(LABEL(data))
    print(data['Close'])
