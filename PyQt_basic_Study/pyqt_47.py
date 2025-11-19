# 예외 처리

import pybithumb
import time
import datetime

with open("C:/Users/0000/Desktop/bithumb.txt") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()
    bithumb = pybithumb.Bithumb(key, secret)

def get_target_price(ticker) :
    df = pybithumb.get_ohlcv(ticker)
    # print(df.tail()) # tail() 메서드를 사용해서 DataFrame 객체에 저장된 일봉 데이터 중 끝의 5개 값만 출력
    yesterday = df.iloc[-2]

    today_open = yesterday['close'] #당일 시가 가져오기
    yesterday_high = yesterday['high'] #전일 고가 가져오기
    yesterday_low = yesterday['low'] #전일 저가 가져오기
    target = today_open + (yesterday_high - yesterday_low) * 0.5 # 목표값 당일시가 + (전일고가 - 전일저가) * 0.5
    return target

# 가격 조회 및 코인구매 정의
def buy_crypto_currency(ticker) :
    krw = bithumb.get_balance("BTC")[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw/float(sell_price)
    bithumb.buy_market_order(ticker, unit)

    # 매도 시도
def sell_crypto_currency(ticker):
    unit = bithumb.get_balance(ticker)[0]
    bithumb.sell_market_order(ticker, unit)

while True :
    try :
        now = datetime.datetime.now()
        if mid < now < mid + datetime.timedelta(second=10):
            target_price = get_target_price("BTC")
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
            sell_crypto_currency("BTC")

        current_price = bithumb.get_current_price("BTC")
        if current_price > target_price:
            buy_crypto_currency("BTC")

    except :
        print("에러 발생")
    time.sleep(1)