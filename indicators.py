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

d = mt5.copy_rates_from_pos(active, mt5.TIMEFRAME_M5, 0, 50)
d = pd.DataFrame(d)
d = timestamptodate(d)
d.set_index('time', inplace=True)

print(d)

print(d.ta.indicators())

# print(help(ta.rsi))
# print(help(ta.bbands))
# print(help(ta.sma))

# Simple
sma21 = ta.sma(d["close"], length=21)
sma51 = ta.sma(d["open"], length=50)

# Exponetial
ema10 = ta.ema(d["close"])

# print(sma21)

sma21.plot()
ema10.plot()

d['close'].plot()
plt.legend(['MMS 21', 'MM 10', 'Closes'])
plt.xlabel('Data')
plt.ylabel("Preço")
plt.figure()

# indexing date
# d.set_index('time', inplace=True)

# RSI
RSI = ta.rsi(d['close'], length=5)
RSI.plot()
plt.title('RSI')

plt.figure()
d['close'].plot()
plt.title('Preço')

plt.show()

