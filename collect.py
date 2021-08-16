import MetaTrader5 as mt5

if mt5.initialize():
    print('Login sucess')
else:
    print('Login error')

n_active = mt5.symbols_total()

print(n_active)

active = mt5.symbols_get()

print(type(active))

print(type(active[0]))

print(active[0]._asdict())

print(active[0].name)

active1 = 'USDJPY'

print(mt5.symbol_info(active1)._asdict())

active2 = 'XYXYX'
info = mt5.symbol_info(active2)

if info != None:
    print(info)
else:
    print('Not found', active2)

active3 = 'XAGUSD'
info1 = mt5.symbol_info(active3)

print('Market observation:', info1.select)

# Add assets in market watch
selection = mt5.symbol_select(active3, True)

# Remove assets on market watch
selection1 = mt5.symbol_select(active3, False)
