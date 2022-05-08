import numpy as np
import pandas as pd

### GARRY ###


def SAR(data: pd.DataFrame) -> np.ndarray:
    pass


def CCI(data: pd.DataFrame) -> np.ndarray:
    pass


def TRANGE(data: pd.DataFrame) -> np.ndarray:
    pass


def EMA(data: pd.DataFrame) -> np.ndarray:
    pass


def STOCH(data: pd.DataFrame) -> np.ndarray:
    pass


def AROON(data: pd.DataFrame) -> np.ndarray:
    pass


def SMA(data: pd.DataFrame) -> np.ndarray:
    pass


def BBANDS(data: pd.DataFrame) -> np.ndarray:
    pass

### BUDI ###


def VMAP(data: pd.DataFrame) -> np.ndarray:
    pass


def OBV(data: pd.DataFrame) -> np.ndarray:
    pass


def MACD(data: pd.DataFrame) -> np.ndarray:
    pass


def AD(data: pd.DataFrame) -> np.ndarray:
    pass


def ADX(data: pd.DataFrame) -> np.ndarray:
    pass


def RSI(data: pd.DataFrame) -> np.ndarray:
    pass


if __name__ == "__main__":
    import pandas as pd
    data = pd.read_csv("./data/data.csv")
    print(data["Open"])
    pass
