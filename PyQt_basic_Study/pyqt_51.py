#매수, 매도 그리고 수익률

import numpy as np
import pybithumb
from pandas import DataFrame

#numpy.where(조건, 조건이 참일때의값, 조건이 거짓일때의 값)

data = {'빗썸' : [100,100,100], '코빗':[90,110,120]}

#학습용 데이터

# df = DataFrame(data)
# df['최저가'] = np.where(df['빗썸'] < df['코빗'], '빗썸', '코빗')
# # 최저가 컬럼 추가 = np.where(조건 : 데이터에서 코빗이 빗썸보다 크면, 참이면 빗썸, 거짓이면 코빗 )
# df.to_excel("거래소.xlsx")

df = pybithumb.get_ohlcv("BTC") #비트코인 데이터 가져오기
df['range'] = (df['high'] - df['low']) * 0.5 #range 컬럼추가 = 최고가 - 최저가 * 0.5(필터)
df['target'] = df['open'] + df['range'].shift(1) #target 컬럼추가 = 시가 + 고저가차이

df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'], 1)
# ror컬럼 추가 고가 > 목표값, 종가 / 목표값, 1

df.to_excel("trade.xlsx")