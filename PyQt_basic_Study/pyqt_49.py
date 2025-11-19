#매수 조건 업데이트

import pybithumb
import datetime
import time

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

# 매도 시도
def sell_crypto_currency(ticker):
    unit = bithumb.get_balance(ticker)[0]
    bithumb.sell_market_order(ticker, unit)

df = pybithumb.get_ohlcv("BTC")
close = df['close']
ma5 = close.rolling(5).mean()
# print(ma5)

# 가격 조회 및 코인구매 정의
def buy_crypto_currency(ticker) :
    krw = bithumb.get_balance("BTC")[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw/float(sell_price)
    bithumb.buy_market_order(ticker, unit)

#전일 5 일 이동평균을 계산
def get_yesterday_ma5(ticker) :
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(window=5).mean()
    return ma.iloc[-2]

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
ma5 = get_yesterday_ma5("BTC")
target_price = get_target_price("BTC")

while True :
    try :
        now = datetime.datetime.now()
        if mid < now < mid + datetime.timedelta(seconds=10):
            target_price = get_target_price("BTC")
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
            ma5 = get_yesterday_ma5("BTC")
            sell_crypto_currency("BTC")

        current_price = pybithumb.get_current_price("BTC")
        if (current_price > target_price) and (current_price > ma5):
            buy_crypto_currency("BTC")

    except :
        print("에러발생")
    time.sleep(1)