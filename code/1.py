'''backtest
start: 2020-06-30 21:30:00
end: 2020-06-30 22:22:00
period: 5s
basePeriod: 5s
exchanges: [{"eid":"Binance","currency":"ETH_USDT"}]
'''
from fmz import *
task = VCtx(__doc__) # initialize backtest engine from __doc__
#需要用的pandas库，并且用自己的托管回测才能保存到本地
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

from drawpic import *
from analyse import *


#保存路径
path = 'C:\\'
def main():
    df=pd.DataFrame()
   # while True:
    records = _C(exchange.GetRecords,PERIOD_D1)

    account = _C(exchange.GetAccount)
    df = pd.DataFrame(records)  #      
    print(df.shape[0])
    df['Time']=pd.to_datetime(df['Time'],unit='ms')+pd.Timedelta('8 h')
    #df.plot(x='Time',y='Close')  dd   vvv
    #plt.show()
    dfbolling = dataAnalyse(df)
    add_plot = [mpf.make_addplot(dfbolling["BBANDS_upper"], color='y'),mpf.make_addplot(dfbolling["BBANDS_middle"], color='r'),mpf.make_addplot(dfbolling["BBANDS_lower"], color='b')]
    plotKLine(df,add_plot)

        #
        # df_new['Time'] = pd.to_datetime(df_new['Time'],unit='ms')+pd.Timedelta('12 h')
        # df_new.index = df_new['Time']
        # if df.empty or df_new['Time'].min() >= df['Time'].max():
        #      df=df.combine_first(df_new)
        #      print(df['Time'].max())
        # #确定最后一次时间，用于保存数据
        # #if df_new['Time'].max() == pd.Timestamp('2017-11-15 23:45:00'):
        #      print('保存1数据')
        #      df=df.combine_first(df_new)
        #      df.to_csv(path+'records14.csv',index=False)
        #      break
        # #休眠时间是选择周期
    #    Sleep(5*60*1000)









try:
    main()
except Exception as e:
    print(e)
    records=task.Join()

