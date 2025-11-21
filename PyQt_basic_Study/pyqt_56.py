# 각 거래일에 대한 기간수익률을 사용한 거래일마다 낙폭 계산 및 낙폭 중 최댓값 찾기
# P.293

import pybithumb
import numpy as np

df = pybithumb.get_ohlcv('BTC')
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.0032
df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'] - fee , 1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

print("MDD(%): ", df['dd'].max())
# 결과 : 거래소에서 변동성 돌파 전략으로 비트코인을 거래시 MDD가 약 84%
df.to_excel("dd.xlsx")

