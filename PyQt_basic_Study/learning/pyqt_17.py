# 판다스 DataFrame2
# p.200 #data read

import pandas as pd
import requests

url = "https://finance.naver.com/item/main.nhn?code=066570"
df = pd.read_html(requests.get(url, headers={'User-agent':'Chrome'}).text)

#console : pip install lxml 의존성추가

# print(df[0])
#                    0  ...                          2
# 0  전일  91,700  91,700  ...  거래량  1,102,710  1,102,710
# 1    시가  91,10091,100  ...   거래대금  97,594  97,594  백만

print(df[0].dropna(axis=0)) # 결과 출력시 NaN이 포함된 행 전체를 삭제
#p.201