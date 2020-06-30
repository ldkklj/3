import mplfinance as mpf
import pandas as pd
def plotKLine(data,add_plot):
    data['Time'] = pd.to_datetime(data['Time'], unit='ms')
    data.index=data['Time']
    data.rename(columns={'open':'Open', 'close':'Close', 'high':'High','low':'Low','Time':'Date'}, inplace = True)
   # mpf.plot(data, type='candle',style='yahoo',figratio=(2,1), figsize=(20,11),mav=(2, 5, 10))
    mpf.plot(data, type='candle', style='yahoo', addplot=add_plot,figratio=(2, 1), figsize=(20, 11))
    print(mpf.available_styles())
