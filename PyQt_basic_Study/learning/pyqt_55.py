#MDD 계산하기
 #mdd = (max-low) / max * 100
 # mdd : 내가 겪을수 있는 최악의 손실 폭 즉 가장 비쌀 때 사서 가장 쌀 때 팔았을 경우, 내 계좌가 얼마나 박살 났을까?
 
import numpy as np
import pybithumb


df = pybithumb.get_ohlcv("BTC") #비트코인 데이터 가져오기

df['range'] = (df['high'] - df['low']) * 0.5 #range 컬럼추가 = 최고가 - 최저가 * 0.5(필터)
df['target'] = df['open'] + df['range'].shift(1) #target 컬럼추가 = 시가 + 고저가차이

fee = 0.0032 # 수수료 0.0032 제외
df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'] - fee, 1) #수익률에서 수수료 제외
# ror컬럼 추가 고가 > 목표값, 종가 / 목표값, 1

#ror 수익률 = df['ror'컬럼].cumprod()[-2] Series 객체에서 끝에서 2번째 값을 ror변수에 바인딩
ror = df['ror'].cumprod()[-2]
df['hpr'] = df['ror'].cumprod()
df.to_excel("btc.xlsx")

#ror 당일수익률
# hpr 기간 수익률