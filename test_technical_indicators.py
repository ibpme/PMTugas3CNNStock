import pandas as pd
import numpy as np

test_data = pd.read_csv('./data/data.csv')

### GARRY ###

def Test_SAR():
    from technical_indicators.sar import SAR
    want = np.array(
        [
            np.nan,
            np.nan, 
            6478.63717096,
            6395.19973071,
            6395.19973071,
            6483.54488397,
            6483.54488397,
            6477.80245588,
            6472.23230062,
            6292.13061412,
            6293.94659819,
            6295.74442243,
            6297.52426842,
            6299.28631595,
            6301.030743,
            6302.75772578,
            6304.46743874,
            6306.16005457,
            6307.83574424,
            6309.49467701,
            6311.13702045,
            6312.76294046,
            6329.5185044,
            6345.77140141,
            6361.53671152,
            6376.82906232,
            6410.38619319,
            6442.26546752,
            6492.91042406
    ])    
    result = SAR(test_data)
    assert np.allclose(want, result, equal_nan=True)

def Test_CCI():
    pass


def Test_TRANGE():
    pass


def Test_EMA():
    pass


def Test_STOCH():
    pass


def Test_AROON():
    pass


def Test_SMA():
    pass


def Test_BBANDS():
    pass

### BUDI ###


def Test_VMAP():
    pass


def Test_OBV():
    pass


def Test_MACD():
    pass


def Test_AD():
    pass


def Test_ADX():
    pass


def Test_RSI():
    pass


if __name__ == '__main__':
    Test_SAR()
    Test_CCI()
    Test_TRANGE()
    Test_EMA()
    Test_STOCH()
    Test_AROON()
    Test_SMA()
    Test_BBANDS()
    Test_VMAP()
    Test_OBV()
    Test_MACD()
    Test_AD()
    Test_ADX()
    Test_RSI()