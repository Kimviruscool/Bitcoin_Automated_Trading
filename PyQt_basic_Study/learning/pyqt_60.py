# 변동성 돌파 + 상승장 전략 백테스팅

import pybithumb
import numpy as np

df = pybithumb.get_ohlcv("BTC") #비트코인의 데이터 가져오기

df['ma5'] = df['close'].rolling(window=5).mean().shift(1) #종가데이터 5일 이동평균을 계산 shift(1) 을 해서 excel에서 표기시 한행밑으로내려 저장
df['range'] = (df['high'] - df['low']) * 0.5 # 고가 - 저가 * 0.5 = 차이값 #차이값 컬럼추가
df['target'] = df['open'] + df['range'].shift(1) #목표값 컬럼 추가 = 시가 + 차이값 #한행 내려서 저장
df['bull'] = df['open'] > df['ma5'] # bull 상승장 컬럼추가 = 거래일의 시가가 전일 종가까지 계산된 5일 이동평균보다 크면 true를 아니면 false를 저장

fee = 0.0032 #수수료 지정
df['ror'] = np.where((df['high'] > df['target']) & df['bull'], df['close'] / df['target'] - fee , 1) #수익률컬럼 추가 numpy 조건사용 (고가가 목표보다 높고 AND bull이 true(상승장)일때 ,(참) 종가 / 목표값 - 수수료 ,거짓 1(현금보유) )

df['hpr'] = df['ror'].cumprod() #기간 수익률, 누적수익률 (HPR) 계산: 일별 수익률(ror)을 모두 곱하여 자산이 어떻게 불어났는지 계산

df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
# 낙폭(Drawdown) 계산: (현재까지의 최고 수익률 - 현재 수익률) / 현재까지의 최고 수익률 * 100
# 설명: 전 고점 대비 현재 자산이 몇 퍼센트 하락했는지를 나타냄

print("MDD :", df['dd'].max())
# MDD 출력: 낙폭(dd) 중 가장 큰 값(최대 낙폭)을 출력
# MDD(최대 낙폭): 투자 기간 중 겪을 수 있는 최악의 손실률

print("HPR :", df['hpr'][-2])
# HPR 출력: 데이터의 뒤에서 두 번째 날짜의 누적 수익률을 출력
# HPR(누적 수익률): 어제 기준 누적 수익률 ([-1]은 오늘 진행 중인 데이터일 수 있어 [-2] 사용)

df.to_excel("larry_ma.xlsx")

# 결과
# MDD : 41.07120419932468 # 낙폭 : 41%
# HPR : 18.63912720313011 # 기간수익률(누적수익률) : 18배 (2013년12월27일 부터 2025년11월20일까지데이터 기준 )

