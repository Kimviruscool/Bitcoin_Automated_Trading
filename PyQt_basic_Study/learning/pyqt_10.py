# 웹스크래핑 웹크롤링

import requests #request패키지 호출
from bs4 import BeautifulSoup #BeatifulSoup4 패키지 호출

# url = "https://www.naver.com"
# response = requests.get(url)

url = "https://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url)

# print(html) #확인용 #결과 : <Response[200]>

#console : pip install html5lib 
# html5lib 모듈추가

soup = BeautifulSoup(html.text, 'html5lib') #html5lib 모듈
tags = soup.select("#_dvr")
tag = tags[0]
print(tag.text)