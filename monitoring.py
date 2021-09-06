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

active = 'EURUSD'

ok = mt5.symbol_select(active, True)

if not ok:
    print("Asset addition failed ", active)
    mt5.shutdown()

cont = 0

while True:

    region = timezone("Etc/UTC")
    d = datetime.now(tz=timezone('America/Sao_Paulo'))
    print(d)

    minutes = d.minute
    hours = d.hour
    seconds = d.second

    if seconds == 59:
        cont += 1
        c = mt5.copy_rates_from_pos(active, mt5.TIMEFRAME_M1, 0, 20)
        c = pd.DataFrame(c)
        c = timestamptodate(c)

        print(c)
        print('New M1 Candle = ', cont)

    time.sleep(1)
