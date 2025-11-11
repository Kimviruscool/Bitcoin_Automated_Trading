# 판다스 DataFrame
# p.197

from pandas import DataFrame

data = {'open' : [100, 200], "high" : [110, 210], "low" : [120, 220], "close" : [130, 230]}
df = DataFrame(data, index=['2018-08-01','2018-08-02']) #index=['이름1','이름2'] 방식으로 인덱스에 이름 추가 가능
print(df)

# 결과
#index  open  high
# 0     100   110
# 1     200   210
#자동 매핑됨

df.to_csv('data.csv')