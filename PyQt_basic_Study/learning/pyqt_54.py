# 가장 좋은 k값 구하기
# k값 = 가장 기간수익률이 높은 것

import pybithumb
import numpy as np

def get_ror(k=0.5):
    df = pybithumb.get_ohlcv("BTC")
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'] - fee, 1)

    ror = df['ror'].cumprod()[-2]
    return ror

#0.1씩 증가시켜서 최고의 k값 - 수익률 계산
for k in np.arange(0.1,1.0,0.1):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))

