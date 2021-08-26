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
active2 = 'USDJPY'

# Add assets in market watch
ok = mt5.symbol_select(active, True)

if not ok:
    print("Asset addition failed ", active)
    mt5.shutdown()

# Copy_rates...
'''
copy_rates_from(
    symbol,
    timeframe, 
    date_from,
    count
    )
'''

c = mt5.copy_rates_from(active, mt5.TIMEFRAME_H4, datetime.now(), 30)

c = pd.DataFrame(c)

c = timestamptodate(c)

'''
copy_rates_from_pos(
    symbol,
    timeframe, 
    start_pos, // initial bar number
    count
    )
'''

c2 = mt5.copy_rates_from_pos(active, mt5.TIMEFRAME_D1, 0, 40)

c2 = pd.DataFrame(c2)

c2 = timestamptodate(c2)

'''
copy_rates_range(
    symbol,
    timeframe, 
    data_from,
    date_to
    )
'''

timezone = pytz.timezone("Etc/UTC")

utc_from = datetime(2021, 7, 15, hour=10, tzinfo=timezone)
utc_to = datetime(2021, 7, 15, hour=16, tzinfo=timezone)

c3 = mt5.copy_rates_range(active, mt5.TIMEFRAME_H1, utc_from, utc_to)

c3 = pd.DataFrame(c3)

c3 = timestamptodate(c3)

# TICKS
lasttick = mt5.symbol_info_tick(active)

# print(lasttick._asdict())

today = datetime.now()

'''
copy_ticks_from(
    symbol,
    date_from, 
    count,
    flags
    )
'''

ticks = mt5.copy_ticks_from(active, today, 50, mt5.COPY_TICKS_INFO)

ticks = pd.DataFrame(ticks)
ticks = timestamptodate_ticks(ticks)

# print(ticks)

filter1 = ticks['flags'] == mt5.TICK_FLAG_BID
filter2 = ticks['volume'] >= 400

# print(ticks.loc[filter1, :])
# print(ticks.loc[filter2, :])

'''
copy_ticks_range(
    symbol,
    date_from, 
    date_to,
    flags
    )
'''

ticks2 = mt5.copy_ticks_range(active, utc_from, utc_to, mt5.COPY_TICKS_ALL)

ticks2 = pd.DataFrame(ticks2)
ticks2 = timestamptodate_ticks(ticks2)

# print(ticks2)

'''
while True:
    last = mt5.symbol_info_tick(active)
    print(last.ask)
    time.sleep(1)
'''

# Indicators
d = mt5.copy_rates_from_pos(active, mt5.TIMEFRAME_M5, 0, 50)
d = pd.DataFrame(d)
d = timestamptodate(d)
d.set_index('time', inplace=True)

# print(d.ta.indicators())

# print(help(ta.rsi))
# print(help(ta.bbands))
# print(help(ta.sma))

# Simple
sma21 = ta.sma(d["close"], length=21)
sma51 = ta.sma(d["open"], length=50)

# Exponetial
ema10 = ta.ema(d["close"])

# print(sma21)
'''
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
'''



