import pandas as pd
import talib as talib


def dataAnalyse(data):
    dftemp = pd.DataFrame()
    dftemp["BBANDS_upper"], dftemp["BBANDS_middle"], dftemp["BBANDS_lower"] = talib.BBANDS(data['Close'].values)
    return dftemp