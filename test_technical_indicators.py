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
        ]
    )    
    result = SAR(test_data)
    assert np.allclose(want, result, equal_nan=True)

def Test_CCI():
    from technical_indicators.cci import CCI
    want = np.array(
        [
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            2.6812540527876623,
            -72.6491418340257,
            -45.570034869575224,
            -55.55568035343966,
            91.93633066251489,
            -86.98270990581541,
            65.50036029313551,
            124.58856514702521,
            62.49927013109563,
            103.93191271928869,
            -30.385589609545473,
            45.808447476081426,
            333.33333333333445,
            138.57675544641825,
            132.00893820445998,
            106.76254656541605,
            140.2685392332011,
            120.81515342271234,
            131.1948329461791,
            105.1085129334176,
        ]
    )    
    result = CCI(test_data)
    assert np.allclose(want, result, equal_nan=True)

def Test_TRANGE():
    from technical_indicators.trange import TRANGE
    want = np.array(
        [
            63.80476001701754,
            117.79339879587133,
            83.43698804450742,
            53.98864142704406,
            34.35640740938925,
            171.78204080332853,
            157.05786244292267,
            68.71281498634107,
            39.2649922083574,
            98.16116787624105,
            63.804759295011536,
            98.16116286057695,
            53.98864034641065,
            78.52893057137408,
            63.8047578456044,
            88.34546885428517,
            44.172522455000944,
            83.4369887320845,
            39.26446440444488,
            58.89669855971988,
            63.804754657223384,
            412.27734375,
            186.50621547360424,
            215.95457861889372,
            83.43699097822173,
            230.6787109375,
            93.25311245199009,
            137.42500294710317,
            58.896701089764974,
        ]
    )
    result = TRANGE(test_data)
    assert np.allclose(want, result, equal_nan=True)
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