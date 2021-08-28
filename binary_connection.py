import MetaTrader5 as mt5
import pandas as pd
import pandas_ta as ta
import time
from datetime import datetime
import pytz
import cufflinks as cf
import plotly
import matplotlib.pyplot as plt


def timestamptodate(df):
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df


def timestamptodate_ticks(df):
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df['time_msc'] = pd.to_datetime(df['time_msc'], unit='ms')
    return df


if mt5.initialize():
    print('Login sucess')
else:
    print('Login error', mt5.last_error())

n_active = mt5.symbols_total()

print(n_active)

'''
active = mt5.symbols_get()
for i in active:
    print(i.name)
'''

active = 'Volatility 75 Index'

ok = mt5.symbol_select(active, True)
print(ok)

if not ok:
    print("Asset addition failed ", active)
    mt5.shutdown()

point = mt5.symbol_info(active).point
price = mt5.symbol_info_tick(active).ask
deviation = 500
lot = 0.02

request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": active,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": price,
    "sl": price - 100000 * point,
    "tp": price + 100000 * point,
    "deviation": deviation,
    "magic": 234000,
    "comment": "BUT AT MARKET",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_FOK
}

result = mt5.order_send(request)

print(result)

print(mt5.last_error())

print("1. order_send(): by {} {} lots at {} with deviation={} points".format(active, lot, price, deviation))
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("2. order_send failed, retcode={}".format(result.retcode))
    result_dict = result.asdict()
    for field in result_dict.keys():
        print("  {}={}".format(field, result_dict[field]))
        if field == "request":
            traderequest_dict = result_dict[field]._asdict()
            for tradereq_filed in traderequest_dict:
                print(" traderesquest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
    
    print("shutfown() and quit")

# Limit

point = mt5.symbol_info(active).point
price = mt5.symbol_info_tick(active).ask - 2000.0
deviation = 500
lot = 0.02

request = {
    "action": mt5.TRADE_ACTION_PENDING,
    "symbol": active,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY_LIMIT,
    "price": price,
    "sl": price - 100000 * point,
    "tp": price + 100000 * point,
    "deviation": deviation,
    "magic": 234000,
    "comment": "BUT AT MARKET",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_FOK
}

rl = mt5.order_send(request)
print(mt5.last_error())
print(rl.retcode)

# mt5.Close(active)

print(mt5.orders_total())
myOrders = mt5.orders_get()
print(myOrders[1])
