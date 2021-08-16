import MetaTrader5 as mt5

if mt5.initialize():
    print('Login sucess')
else:
    print('Login error')

n_ativos = mt5.symbols_total()

print(n_ativos)

ativos = mt5.symbols_get()

print(type(ativos))

print(type(ativos[0]))

print(ativos[0]._asdict())

print(ativos[0].name)

for i in ativos:
    print(i.name)

