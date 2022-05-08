import yfinance as yf
import numpy as np
yfObj = yf.Ticker('BBCA.JK')
data = yfObj.history(start='2021-09-01', end='2021-10-12')

def Test_SAR():
    from technical_indicators.sar import SAR
    want = np.array([
        np.nan,
        np.nan,
        6395.200213,
        6336.303725,
        6340.720965,
        6483.545030,
        6483.544884,
        6477.802456,
        6472.232301,
        6292.130614,
        6293.946598,
        6295.744422,
        6297.524268,
        6299.286316,
        6301.030743,
        6302.757726,
        6304.467439,
        6306.160055,
        6307.835744,
        6312.812544,
        6317.640039,
        6322.322710,
        6349.770661,
        6375.846215,
        6400.617991,
        6424.151178,
        6467.818614,
        6508.429328,
        6567.58956,
    ])
    result = SAR(data)
    assert result == want


Test_SAR()