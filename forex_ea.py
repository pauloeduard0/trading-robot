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
        "type_filling": mt5.ORDER_FILLING_IOC,
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
        "type_filling": mt5.ORDER_FILLING_IOC,
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
        "type_filling": mt5.ORDER_FILLING_IOC,
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
        "type_filling": mt5.ORDER_FILLING_IOC,
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


def positioned(active):
    positions = mt5.positions_get(symbol=active)

    pos = False
    if positions is None:
        pos = False
    elif len(positions) > 0:
        pos = True
    return pos


def can_trade(io, lo):
    filter1 = datetime.now().strftime("%H:%M:%S") >= io
    filter2 = datetime.now().strftime("%H:%M:%S") <= lo
    resp = filter1 & filter2
    return resp


if mt5.initialize():
    print('Login sucess')
else:
    print('Login error', mt5.last_error())

active = 'EURUSD'

ok = mt5.symbol_select(active, True)

if not ok:
    print("Asset addition failed ", active)
    mt5.shutdown()

# Hours
initial_operation = '10:30'
limit_operation = '23:55'
limit_close_postion = '23:50'

# IFR
sobre_compra = 52
sobre_venda = 48
period_IFR = 7

# parameters
lotes = 0.01
stoploss = 0.00005
takeprofit = 0.00005

versao_EA = '1.00'
contm = 0  # contador de minutos operacionais do robô
position = ''

while True:
    region = timezone("Etc/UTC")
    d = datetime.now(tz=timezone('America/Sao_Paulo'))

    if can_trade(initial_operation, limit_operation):
        # d = datetime.now()
        m = d.minute
        h = d.hour
        s = d.second

        if not positioned(active):
            print(active, "Waiting... Date/Time = ", d)
        else:
            tick = mt5.symbol_info_tick(active).ask
            if position == 'SELL':
                print(s, ' - SELL : Price = ', tick, ", TP: ", v.request.tp, ", SL: ", v.request.sl),
            if position == 'BUY':
                print(s, ' - BUY : Price = ', tick, ", TP: ", c.request.tp, ", SL: ", c.request.sl)

        if s == 59:
            contm += 1

            c2 = mt5.copy_rates_from_pos(active, mt5.TIMEFRAME_M1, 0, period_IFR + 5)
            c2 = pd.DataFrame(c2)
            c2 = timestamptodate(c2)

            IFR = ta.rsi(c2['close'], length=period_IFR)

            if (IFR.iloc[-1] >= sobre_compra) & (positioned(active) == False):
                print('Sell! -> IFR >= ', sobre_compra)
                v = sell_market(active, takeprofit, stoploss, lotes)
                position = 'SELL'

            if (IFR.iloc[-1] <= sobre_venda) & (positioned(active) == False):
                print('BUY! -> IFR <= ', sobre_venda)
                c = buy_market(active, takeprofit, stoploss, lotes)
                position = 'BUY'

            print('IFR = ', IFR.iloc[-1], ", Sobre COMPRA: ", sobre_compra, ", Sobre VENDA: ", sobre_venda)

        if positioned(active) & (d.strftime("%H:%M:%S") >= limit_close_postion):
            close_position(active)
            posicao = ''
            print('Close Position')

        time.sleep(1)

    else:
        print('Attention! Out of Hours', datetime.now())

        if positioned(active) & (d.strftime("%H:%M:%S") >= limit_close_postion):
            close_position(active)
            posicao = ''
            print('Close Position')

        time.sleep(10)
