#상승장과 하락장 구분하는 함수 구현하기

# 현재가가 전일 이동평균보다 높으면 상승장 낮으면 하락장으로 판단.
import pybithumb #pybithum 모듈호출

df = pybithumb.get_ohlcv("BTC") #비트코인의 시가,고가,저가,종가,거래량 호출
ma5 = df['close'].rolling(window=5).mean() #이동평균계산하기 window=5 5일단위로 그룹화
last_ma5 = ma5[-2] #그룹화된 데이터중 뒤에서2번째 데이터 호출

price = pybithumb.get_current_price("BTC") #현재 비트코인 가격 호출

# 비교하기
if price > last_ma5: #만약 가격이 어제 가격보다 높다면 상승장
    print("상승장")
else: # 만약 가격이 어제 가격보다 낮다면 하락장
    print('하락장')
