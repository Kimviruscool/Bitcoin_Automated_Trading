#지갑 조회와 매도


import pybithumb

con_key = "??"
sec_key = "??"

bithumb = pybithumb.Bithumb(con_key, sec_key)

krw = bithumb.get_balance("BTC")[2] #내 잔고조회
print(krw)

orderbook = bithumb.get_orderbook("BTC") #주문할 코인정보
asks = orderbook["asks"]
sell_price = asks[0]["price"] #주문할 코인의 현재가격 1코인의 가격
print(float(sell_price))

unit = krw/float(sell_price) # 몇개 구매가능한지 확인
print(f'{unit:.8f}')

order = bithumb.sell_limit_order("BTC", 4000000, 1)
print(order)