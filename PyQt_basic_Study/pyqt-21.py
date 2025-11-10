#pybithum 상승장 알리미 p.208

import pybithumb
import time

#티커 목록 얻기 (Ticker = 가상화폐 구분코드 비트코인 : BTC)
tickers = pybithumb.get_tickers()
print(tickers)

print(len(tickers)) #435개

#현재가 얻어오기
price = pybithumb.get_current_price("BTC")
print(price,"Won") #157120000 현재가

#1초 마다 갱신
# while True :
#     price = pybithumb.get_current_price("BTC")
#     print(price,"Won")
#     time.sleep(1)

# 모든 코인가격 확인하기

for ticker in tickers :
    price = pybithumb.get_current_price(ticker)
    print(ticker, price)
    time.sleep(1)
