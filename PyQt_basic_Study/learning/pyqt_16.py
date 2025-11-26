# 판다스 DataFrame2
# p.200 #data read

import pandas as pd

df = pd.read_csv('../file/data.csv')
# pd.read_excel('data.xlsx') 엑셀 타입도 가능
print(df)