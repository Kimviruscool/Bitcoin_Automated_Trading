# 변동성 돌파 전략 구현

# 가격 변등폭 계산 : 투자하려는 가상화폐의 전일 고가에서 전일 저가를 빼서 가상화폐의 가겨변등폭을 구한다.
# 매수 기준 : 당일 시간에서 (변등폭 * 0.5) 이상 상승하면 해당 가격에 바로 매수
# 매도 기준 : 당일 종가에 매도
# 0 모듈
import pybithumb
import time
import datetime

# 1 주기적으로 현재가 얻어오기

# while True:
#     price = pybithumb.get_current_price("BTC")
#     print(price)
#     time.sleep(0.2)

# 2 목표가 계산하기 / def
def get_target_price(ticker) :
    df = pybithumb.get_ohlcv(ticker)
    # print(df.tail()) # tail() 메서드를 사용해서 DataFrame 객체에 저장된 일봉 데이터 중 끝의 5개 값만 출력
    yesterday = df.iloc[-2]

    today_open = yesterday['close'] #당일 시가 가져오기
    yesterday_high = yesterday['high'] #전일 고가 가져오기
    yesterday_low = yesterday['low'] #전일 저가 가져오기
    target = today_open + (yesterday_high - yesterday_low) * 0.5 # 목표값 당일시가 + (전일고가 - 전일저가) * 0.5
    return target

# 3 자정에 목표가 갱신하기

# dt = datetime.datetime(2018, 12, 1)
# print(dt)
# print(dt.year, dt.month, dt.day)

now = datetime.datetime.now()
print(now) #현재시간 확인

mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
print(mid) # 다음날 정각으로 만들기

# 반복
while True :
    now = datetime.datetime.now()
    if mid < now < mid + datetime.timedelta(seconds=10) : #datetime.delta(second=10) 10초를 더한다 # 자정기준
        print("정각입니다.")
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

    time.sleep(1)
