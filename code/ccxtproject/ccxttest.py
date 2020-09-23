#import ccxtpro
import ccxt
#mport queue
import pandas as pd
import time

CONST_INTERVEL =1
CONST_LISTLEN  =180/CONST_INTERVEL

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
biance.load_markets()
tradepairs=biance.markets   #获取所有合约的交易对





class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value
records = Vividict()

#records={}
records.fromkeys(tradepairs)
for key in tradepairs:
    records[key]['data'] = []

def updateTicks(alltrades): #获取所有交易对行情
    try:
        tickers = biance.fetch_tickers(symbols=alltrades)
    except Exception as e:
        print('get tickers time out:', e)
        return
    for key in tickers:
        if key in records:
            singleRecord={}
            singleRecord['time']=tickers[key]['timestamp']
            singleRecord['price']=tickers[key]['last']
            if singleRecord['price'] is not None:
                if len(records[key]['data'])>CONST_LISTLEN:
                    del records[key]['data'][0]
                records[key]['data'].append(singleRecord)

def analyse(): #进行分析，给出买卖提示
    if len(records['BTC/USDT']['data'])!=CONST_LISTLEN
        return
    for key in records:
        tempkeymin = min(records[key]['data'], key=lambda x: x['price'])
        minIndex = records[key]['data'].index(tempkeymin)
        tempkeymax = max(records[key]['data'], key=lambda x: x['price'])
        maxIndex = records[key]['data'].index(tempkeymax)
        midPrice = (tempkeymax['price'] + tempkeymin['price'])/2
        deltaPrice = tempkeymax['price'] - tempkeymin['price']
        deltaRatio = deltaPrice /midPrice

        # 条件一：跌幅超过1% 条件2 下降趋势 条件3 最低值保持15秒以上
        # 即使取得最小值，仍需至少等待15秒并判断这15秒的值是否有上升趋势
        if deltaRatio>0.01 and deltaMSecs < 0 and minIndex>(CONST_LISTLEN-15):
            ltime = time.localtime(tempkeymin['time'])
            strltime = time.strftime("%Y-%m-%d %H:%M:%S", ltime)
            print("%s----%s---%0.2f---%0.2f" % (key, strltime, tempkeymax['price'], deltaRatio))
            deltaMSecs = tempkeymax['time']-tempkeymin['time']

            dPrice1 = records[key]['data'][-1]['price']-tempkeymin['price']-midPrice*0.005
            dPrice2 = records[key]['data'][-6]['price']-tempkeymin['price']-midPrice*0.005
            dPrice3 = records[key]['data'][-11]['price']-tempkeymin['price']-midPrice*0.005
            if dPrice1>0 and dPrice2 >0 and dPrice3 >0 :




# def updateTick(tradepair):  # 更新行情
#     q=queue.Queue(180)  #存储180秒的数据
#     try:
#         ticker = biance.fetch_ticker('BTC/USDT')
#     except Exception as e:
#         print('get ticker time out:', e)
#         return
#     singleRecord={}
#     singleRecord['time']=ticker['timestamp']
#     singleRecord['price']=ticker['last']
#     if q.full():
#         q.get()
#     q.put(singleRecord)
    # assets['USDT']['short_value'] = 0
    # assets['USDT']['long_value'] = 0
    # for i in range(len(ticker)):
    #     pair = ticker[i]['symbol']
    #     coin = pair[0:len(pair) - 4]
    #     if coin not in symbols:
    #         continue
    #     assets[coin]['ask_price'] = float(ticker[i]['askPrice'])
    #     assets[coin]['bid_price'] = float(ticker[i]['bidPrice'])
    #     assets[coin]['ask_value'] = _N(assets[coin]['amount'] * assets[coin]['ask_price'], 2)
    #     assets[coin]['bid_value'] = _N(assets[coin]['amount'] * assets[coin]['bid_price'], 2)
    #     if coin not in trade_symbols:
    #         continue
    #     if assets[coin]['amount'] < 0:
    #         assets['USDT']['short_value'] += abs((assets[coin]['ask_value'] + assets[coin]['bid_value']) / 2)
    #     else:
    #         assets['USDT']['long_value'] += abs((assets[coin]['ask_value'] + assets[coin]['bid_value']) / 2)
    #     assets['USDT']['short_value'] = _N(assets['USDT']['short_value'], 0)
    #     assets['USDT']['long_value'] = _N(assets['USDT']['long_value'], 0)
    # updateIndex()
    # for i in range(len(trade_symbols)):
    #     assets[trade_symbols[i]]['btc_diff'] = _N(assets[trade_symbols[i]]['btc_change'] - index, 4)
#updateTick('BTC/USDT')

def main():
    while True:
        updateTicks(tradepairs)
        analyse()
        time.sleep(CONST_INTERVEL)


try:
    main()
except Exception as e:
    print(e)