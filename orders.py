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

active = 'EURUSD'

ok = mt5.symbol_select(active, True)

if not ok:
    print("Asset addition failed ", active)
    mt5.shutdown()

# BUY

point = mt5.symbol_info(active).point
price = mt5.symbol_info_tick(active).ask
deviation = 500
lot = 0.1

request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": active,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": price,
    "sl": price - 100 * point,
    "tp": price + 100 * point,
    "deviation": deviation,
    "magic": 234000,
    "comment": "BUT AT MARKET",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}

result = mt5.order_send(request)

print(result)

print(mt5.last_error())

# SELL

point = mt5.symbol_info(active).point
price = mt5.symbol_info_tick(active).bid
deviation = 500
lot = 0.1

request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": active,
    "volume": lot,
    "type": mt5.ORDER_TYPE_SELL,
    "price": price,
    "sl": price + 100 * point,
    "tp": price - 100 * point,
    "deviation": deviation,
    "magic": 234000,
    "comment": "SELL AT MARKET",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}

result2 = mt5.order_send(request)

print(result2)

print(mt5.last_error())
