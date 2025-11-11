# 웹스크래핑 웹크롤링 3
# 아이디가 없는 태그 스크래핑

import requests #request패키지 호출
from bs4 import BeautifulSoup #BeatifulSoup4 패키지 호출

url = "https://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text

soup = BeautifulSoup(html, 'html5lib') #html5lib 모듈
# tags = soup.select(".lwidth tbody .strong td em") #외국인 소진률 #p.182 #ver1
tags = soup.select("#tab_con1 > div:nth-of-type(2) > table > tbody > tr.strong > td > em") # ver2 #p.184

for tag in tags:
    print(tag.text)
