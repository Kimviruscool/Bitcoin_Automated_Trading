#지갑 조회와 주문


import pybithumb
import time

con_key = "??"
sec_key = "??"

bithumb = pybithumb.Bithumb(con_key, sec_key)

# 지갑조회
balance = bithumb.get_balance("BTC")
print(balance)
print(format(balance[0], 'f'))

# for ticker in pybithumb.get_tickers():
    # balance = bithumb.get_balance(ticker)
    # print(ticker, ":", balance)
    # time.sleep(0.1)
    
# 주문하기
#지정가 매수 .buy.limit_order
order = bithumb.buy_limit_order("BTC",60000000,0.0001)
print(order)
#시장가 매수 .buy_market_order
order =  bithumb.buy_market_order("BTC",1)
print(order)


