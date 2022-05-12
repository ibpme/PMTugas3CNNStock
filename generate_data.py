import pandas as pd
import numpy as np
from technical_indicators.ad import AD
from technical_indicators.adx import ADX
from technical_indicators.aroon import AROON
from technical_indicators.bbands import BBANDS
from technical_indicators.cci import CCI
from technical_indicators.ema import EMA
from technical_indicators.macd import MACD
from technical_indicators.obv import OBV
from technical_indicators.roc import ROC
from technical_indicators.rsi import RSI
from technical_indicators.sar import SAR
from technical_indicators.sma import SMA
from technical_indicators.stoch import STOCH
from technical_indicators.trange import TRANGE
from technical_indicators.vwap import VWAP
from label import LABEL
import yfinance as yf

if __name__ == "__main__":
    ticker = yf.Ticker("IBM")
    
    # get historical market data
    data = ticker.history(period="max")
    
    ta = []
    aroon_u, aroon_l = AROON(data)
    m,u,l = BBANDS(data)
    ta.append(AD(data))
    ta.append(aroon_u)
    ta.append(aroon_l)
    ta.append(m)
    ta.append(u)
    ta.append(l)
    ta.append(CCI(data))
    ta.append(EMA(data))
    ta.append(MACD(data))
    ta.append(OBV(data))
    # ta.append(ROC(data))
    # ta.append(RSI(data))
    ta.append(SAR(data))
    ta.append(SMA(data))
    slow_k, slow_d = STOCH(data)
    ta.append(slow_k)
    ta.append(slow_d)
    ta.append(TRANGE(data))
    ta.append(VWAP(data))
    label = LABEL(data)
    df_dict = {}
    for index, i in enumerate((ta)):
        df_dict[index] = i
    df = pd.DataFrame(df_dict)
    df['label'] = label
    df.to_csv('tech_analysis.csv', index = False)