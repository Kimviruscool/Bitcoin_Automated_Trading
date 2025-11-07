# 웹스크래핑 웹크롤링 2
# 배당수익률과 per 배수 구하기

import requests #request패키지 호출
from bs4 import BeautifulSoup #BeatifulSoup4 패키지 호출

def get_per(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, 'html5lib')
    tags = soup.select("#_per")
    tag = tags[0]
    return float(tag.text)

def get_dividend(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, 'html5lib')
    tags = soup.select("#_dvr")
    tag = tags[0]
    return float(tag.text)

print(get_dividend("000660"))
print(get_per("000660"))