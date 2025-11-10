# 거래소 거래 정보

import pybithumb
import datetime

detail = pybithumb.get_market_detail("BTC")
print(detail, "\n")
# (153147000.0, 158314000.0, 153088000.0, 157448000.0, 468.34921169)
#   시가          고가          저가      종가             거래량

#호가
orderbook = pybithumb.get_orderbook("BTC")
print(orderbook, "\n")

for k in orderbook:
    print(k,"\n")

print(orderbook['payment_currency']) #지원하는 화폐

# print(orderbook['timestamp']) #내가 호가 조회한 시간 #p.215참고
ms = int(orderbook['timestamp'])
dt = datetime.datetime.fromtimestamp(ms/1000)
print(dt)

print(orderbook['order_currency'])  #내가 조회한 가상화폐

print(orderbook['bids']) #매도 호가
# [{'price': 157183000.0, 'quantity': 0.0001}, {'price': 157182000.0, 'quantity': 0.0086}, {'price': 157180000.0, 'quantity': 0.0043}, {'price': 157172000.0, 'quantity': 0.0006}, {'price': 157171000.0, 'quantity': 0.0065}]
# price : 현재기준가격 , quantity : 구매갯수
# 해석 : 157183000 가격일때 0.0001개 구매

print(orderbook['asks']) #매수 호가
#[{'price': 157184000.0, 'quantity': 0.0126}, {'price': 157199000.0, 'quantity': 0.0103}, {'price': 157200000.0, 'quantity': 0.377}, {'price': 157202000.0, 'quantity': 0.0086}, {'price': 157219000.0, 'quantity': 0.0156}]
# quantity : 매수잔량 , price : 매수호가
# 해석 : 157183000 가격일때 0.0126개 판매

#전체 가격정보 얻기
all = pybithumb.get_current_price("ALL")
for ticket, data in all.items():
    print(ticket,data['closing_price'])


#딕셔너리 객체 각 key의미 정리
# opening_price : 시가 00시 기준
# closing_price : 종가 00시 기준
# min_price : 저가 00시 기준
# max_price : 고가 00시 기준
# acc_trade_value : 거래량 00시 기준
# units_traded : 거래량 00시 기준
# prev_closing_price : 전일종가
# utnis_traded_24H : 최근 24시간 거래량
# acc_trade_value_24H : 최근 24시간 거래금액
# fluctate_24H : 최근 24시간 변동가
# fluctate_rate24H : 최근 24시간 변동률

