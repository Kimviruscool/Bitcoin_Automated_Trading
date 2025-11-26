#백테스팅을 위한 데이터 준비
import pybithumb

df = pybithumb.get_ohlcv("BTC")
#레인지 계산하기
df['range'] = (df['high'] - df['low']) * 0.5

# # 가독성을 위한 기능 추가
# df['range_shift'] = df['range'].shift(1)

#목표가 계산하기 (target 추가)
#목표가 계산은 각 거래일을 기준으로 전날의 레인지를 사용하기 때문에 'rage'의 컬럼을 1행씩(1줄씩)내려주는것
df['target'] = df['open'] + df['range'].shift(1)

df.to_excel("btc.xlsx")


