import MetaTrader5 as mt5
import pandas as pd
import time
from datetime import datetime


def timestamptodate(df):
    df['time'] = pd.to_datetime(df['time'], unit='s')
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

'''
copy_rates_from(
    symbol,
    timeframe, 
    date_from,
    count
    )
'''

c = mt5.copy_rates_from(active, mt5.TIMEFRAME_H4, datetime.now(), 30)

df = pd.DataFrame(c)

dt = timestamptodate(df)

print(dt)

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

print(c2)