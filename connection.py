import MetaTrader5 as mt5

print(mt5.__version__)

# login, server, password
# mt5.initialize(login=51649512, server='ICMarketsSC-Demo', password='Kj349Qjf')

if mt5.initialize():
    print('Login success')
else:
    print('Login error', mt5.last_error())

print(mt5.terminal_info())
print(mt5.version())

mt5.shutdown()
