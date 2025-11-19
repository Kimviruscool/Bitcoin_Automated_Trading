# 변동성 돌파 + 상승장 투자 전략 구현
import pybithumb

df = pybithumb.get_ohlcv("BTC")
close = df['close']
ma5 = close.rolling(5).mean()
print(ma5)

def get_yesterday_ma5(ticker) :
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(window=5).mean()
    return ma.iloc[-2]

get_yesterday_ma5("BTC")
print(get_yesterday_ma5("BTC"))