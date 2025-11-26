#보유중인 비트코인수량만큼 지정가 매도


import pybithumb

con_key = "??"
sec_key = "??"

bithumb = pybithumb.Bithumb(con_key, sec_key)

unit = bithumb.get_balance("BTC")[0]
print(unit)

order = bithumb.sell_limit_order("BTC", 4000000, unit)
print(order)
