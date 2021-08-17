import MetaTrader5 as mt5
import pandas as pd
import time
from datetime import datetime
import pytz

import pytz


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

c = pd.DataFrame(c)

c = timestamptodate(c)

print(c)

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

print(c3)
