import MetaTrader5 as mt5
import pandas as pd
import time
from datetime import datetime
import pytz
import cufflinks as cf
import plotly


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

timezone = pytz.timezone("Etc/UTC")

utc_from = datetime(2021, 7, 15, hour=10, tzinfo=timezone)
utc_to = datetime(2021, 7, 15, hour=16, tzinfo=timezone)

ticks2 = mt5.copy_ticks_range(active, utc_from, utc_to, mt5.COPY_TICKS_ALL)

ticks2 = pd.DataFrame(ticks2)
ticks2 = timestamptodate_ticks(ticks2)

# print(ticks2)

while True:
    last = mt5.symbol_info_tick(active)
    print(last.ask)
    time.sleep(1)

