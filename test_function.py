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


def buy_market(active, tp, sl, lot, desc="Buy Market"):
    point = mt5.symbol_info(active).point
    price = mt5.symbol_info_tick(active).ask
    deviation = 5

    if tp != 0:
        TP = price + tp
    else:
        TP = 0

    if sl != 0:
        SL = price - sl
    else:
        SL = 0

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": active,
        "volume": float(lot),
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "sl": float(SL),
        "tp": float(TP),
        "deviation": deviation,
        "magic": 234000,
        "comment": desc,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_FOK,
    }

    result = mt5.order_send(request)

    print("1. order_send(): by {} {} lots at {} with deviation={} points".format(active, lot, price, deviation))
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("2. order_send failed, retcode={}".format(result.retcode))
        result_dict = result._asdict()
        for field in result_dict.keys():
            print("  {}={}".format(field, result_dict[field]))
            if field == "request":
                traderequest_dict = result_dict[field]._asdict()
                for tradereq_filed in traderequest_dict:
                    print(" traderesquest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))

        print("shutfown() and quit")
    return result


def sell_market(active, tp, sl, lot, desc="Sell Market"):
    point = mt5.symbol_info(active).point
    price = mt5.symbol_info_tick(active).bid
    deviation = 5

    if tp != 0:
        TP = price - tp
    else:
        TP = 0

    if sl != 0:
        SL = price + sl
    else:
        SL = 0

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": active,
        "volume": float(lot),
        "type": mt5.ORDER_TYPE_SELL,
        "price": price,
        "sl": float(SL),
        "tp": float(TP),
        "deviation": deviation,
        "magic": 234000,
        "comment": desc,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_FOK,
    }

    result = mt5.order_send(request)

    print("1. order_send(): by {} {} lots at {} with deviation={} points".format(active, lot, price, deviation))
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("2. order_send failed, retcode={}".format(result.retcode))
        result_dict = result._asdict()
        for field in result_dict.keys():
            print("  {}={}".format(field, result_dict[field]))
            if field == "request":
                traderequest_dict = result_dict[field]._asdict()
                for tradereq_filed in traderequest_dict:
                    print(" traderesquest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))

        print("shutfown() and quit")
    return result


def buy_limit(active, entrada, tp, sl, lot, desc="Buy Limit"):
    point = mt5.symbol_info(active).point
    price = mt5.symbol_info_tick(active).ask
    deviation = 5

    if tp != 0:
        TP = entrada + tp
    else:
        TP = 0

    if sl != 0:
        SL = entrada - sl
    else:
        SL = 0

    request = {
        "action": mt5.TRADE_ACTION_PENDING,
        "symbol": active,
        "volume": float(lot),
        "type": mt5.ORDER_TYPE_BUY_LIMIT,
        "price": entrada,
        "sl": float(SL),
        "tp": float(TP),
        "deviation": deviation,
        "magic": 234000,
        "comment": desc,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_FOK,
    }

    result = mt5.order_send(request)

    print("1. order_send(): by {} {} lots at {} with deviation={} points".format(active, lot, price, deviation))
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("2. order_send failed, retcode={}".format(result.retcode))
        result_dict = result._asdict()
        for field in result_dict.keys():
            print("  {}={}".format(field, result_dict[field]))
            if field == "request":
                traderequest_dict = result_dict[field]._asdict()
                for tradereq_filed in traderequest_dict:
                    print(" traderesquest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))

        # print("shutfown() and quit")
        # mt5.shutdown()
    return result


def sell_limit(active, entrada, tp, sl, lot, desc="Sell Limit"):
    point = mt5.symbol_info(active).point
    price = mt5.symbol_info_tick(active).bid
    deviation = 5

    if tp != 0:
        TP = entrada - tp
    else:
        TP = 0

    if sl != 0:
        SL = entrada + sl
    else:
        SL = 0

    request = {
        "action": mt5.TRADE_ACTION_PENDING,
        "symbol": active,
        "volume": float(lot),
        "type": mt5.ORDER_TYPE_SELL_LIMIT,
        "price": price,
        "sl": float(SL),
        "tp": float(TP),
        "deviation": deviation,
        "magic": 234000,
        "comment": desc,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_FOK,
    }

    result = mt5.order_send(request)

    print("1. order_send(): by {} {} lots at {} with deviation={} points".format(active, lot, price, deviation))
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("2. order_send failed, retcode={}".format(result.retcode))
        result_dict = result._asdict()
        for field in result_dict.keys():
            print("  {}={}".format(field, result_dict[field]))
            if field == "request":
                traderequest_dict = result_dict[field]._asdict()
                for tradereq_filed in traderequest_dict:
                    print(" traderesquest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
        # print("shutfown() and quit")
        # mt5.shutdown()
    return result


def cancel_order():
    request_cancel = {
        "order": mt5.orders_get()[0].ticket,
        "action": mt5.TRADE_ACTION_REMOVE
    }

    result = mt5.order_send(request_cancel)

    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("2. order_send failed, retcode={}".format(result.retcode))
        result_dict = result._asdict()
        for field in result_dict.keys():
            print("  {}={}".format(field, result_dict[field]))
            if field == "request":
                traderequest_dict = result_dict[field]._asdict()
                for tradereq_filed in traderequest_dict:
                    print(" traderesquest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
        # print("shutfown() and quit")
        # mt5.shutdown()
    return result


def close_position(active):
    resp = mt5.Close(active)
    return resp


if mt5.initialize():
    print('Login sucess')
else:
    print('Login error', mt5.last_error())

active = 'Volatility 75 Index'

ok = mt5.symbol_select(active, True)

if not ok:
    print("Asset addition failed ", active)
    mt5.shutdown()

# active, entrada, tp, sl, lot
R1 = buy_market(active, 5000.0, 5000.0, 0.01)
print(R1)

close_position(active)
