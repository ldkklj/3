#import ccxtpro
import ccxt
import pandas as pd

print(ccxt.exchanges)

# huobi =ccxt.binance({
#     'proxies': {
#         'http': 'http://hk1.sgateway.link:706',  # these proxies won't work for you, they are here for example
#         'https': 'https://hk1.sgateway.link:706',
#     },
# })
#huobi = ccxt.huobipro()
#huobi.apiKey='nbtycf4rw2-1b169836-b567486a-26fda'
#huobi.secret='9da5a95d-5aa90559-83b540fb-e0e69'
#huobi.hostname='api.btcgateway.pro'
#huobi.proxies='https://127.0.0.1:1080'

##print(balance)

# huobi.load_markets()
# data = huobi.markets()
# data1 =data

biance = ccxt.binance()
biance.apiKey='vc80GCBbsx4iWZ5fzJVCn3pn5Aczybj9mKsdGuWeJFbhVPmpyjrmsYjj9qRKn69y'
biance.secret='0jKZL2cSBof1TejOq7kdJ34BgVxegZ6MJ9Bi3P8poAKfAH5qkd1Ub7rFxhlRbuXK'
biance.options['defaultType']='future'
#biance.options['defaultType']='swap'
biance.load_markets()
tradepairs=pd.DataFrame()
#tradepairs={}
tradepairs=pd.DataFrame(biance.markets())
import random
print(tradepairs.key())


# def updateTick():  # 更新行情
#     try:
#         ticker = biance.fetch_ticker()
#     except Exception as e:
#         Log('get ticker time out:', e)
#         return
#     assets['USDT']['short_value'] = 0
#     assets['USDT']['long_value'] = 0
#     for i in range(len(ticker)):
#         pair = ticker[i]['symbol']
#         coin = pair[0:len(pair) - 4]
#         if coin not in symbols:
#             continue
#         assets[coin]['ask_price'] = float(ticker[i]['askPrice'])
#         assets[coin]['bid_price'] = float(ticker[i]['bidPrice'])
#         assets[coin]['ask_value'] = _N(assets[coin]['amount'] * assets[coin]['ask_price'], 2)
#         assets[coin]['bid_value'] = _N(assets[coin]['amount'] * assets[coin]['bid_price'], 2)
#         if coin not in trade_symbols:
#             continue
#         if assets[coin]['amount'] < 0:
#             assets['USDT']['short_value'] += abs((assets[coin]['ask_value'] + assets[coin]['bid_value']) / 2)
#         else:
#             assets['USDT']['long_value'] += abs((assets[coin]['ask_value'] + assets[coin]['bid_value']) / 2)
#         assets['USDT']['short_value'] = _N(assets['USDT']['short_value'], 0)
#         assets['USDT']['long_value'] = _N(assets['USDT']['long_value'], 0)
#     updateIndex()
#     for i in range(len(trade_symbols)):
#         assets[trade_symbols[i]]['btc_diff'] = _N(assets[trade_symbols[i]]['btc_change'] - index, 4)
