import MetaTrader5 as mt5
import pandas as pd
import pandas_ta as ta
import time
from datetime import datetime
import pytz
import cufflinks as cf
import plotly
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import timezone


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

active = 'Volatility 75 Index'

ok = mt5.symbol_select(active, True)
print(ok)

if not ok:
    print("Asset addition failed ", active)
    mt5.shutdown()

i = 0

while i <= 2:
    i += 1
    print(i)
    time.sleep(1)

d = datetime.now(tz=timezone('America/Sao_Paulo'))
print(d)
print(type(d))
print(d.minute)
print(d.second)