# 상승장 알리미

import pybithumb

btc = pybithumb.get_ohlcv("BTC") #open,high,low,close,volume 값가져오기
close = btc['close'] # close 값 변수에 바인딩

# 이동평균 계산하기

# 방법1 : Dataframe에서 종가를 얻어오고 인덱싱(번호를 사용하여 호출) 하여 다섯개 값을 호출
# 5일 이동평균선 세 개
# print((close[0]+close[1]+close[2]+close[3]+close[4])/5)
# print((close[1]+close[2]+close[3]+close[4]+close[5])/5)
# print((close[2]+close[3]+close[4]+close[5]+close[6])/5)

#방법2 : rolling , mean() 사용
window = close.rolling(5) #모든 종가의 데이터를 호출후 5일씩 데이터를 그룹화 하여 저장
ma5 = window.mean() #그룹화된 값의 평균을 구함
print(ma5)

#축약 방법 ma5 = close.rolling(5).mean()



