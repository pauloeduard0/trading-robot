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

print(lasttick._asdict())

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

print(ticks)
