#변동성 돌파전략 구현

#빗썸 Bithumb API 활용
# 잔고조회 p.252

import pybithumb

#use your API Key
con_key = "??"
sec_key = "??"

bithumb = pybithumb.Bithumb(con_key, sec_key)

balance = bithumb.get_balance("BTC")
print(balance)
print(format(balance[0], 'f'))