#수수료 및 슬리피지를 고려한 백테스팅

# 슬리피지 : 주문을 넣을 때 거래량 부족으로 인해 여러분이 생각하는 가격대보다 조금 더 비싸게 매수되거나 조금더 싸게 매도될수있는데 이때 발생하는 비용을 슬리피지라고한다.

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

print(ror) 