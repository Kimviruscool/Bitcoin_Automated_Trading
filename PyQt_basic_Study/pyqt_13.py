# Restful API
# p.188

# 웹에서 데이터를 얻어오는 방법2
# 웹 API를 사용하는 방법

# API adress (korbit)
# https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw

# xrp_krw (리플의 현재가)
# https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=xrp_krw

# key 정리
# timestamp 최종 체결 시각
# last 최종 체결 가격
# bid 최우선 매수호가 (매수 수문 중 가장 높은 가격)
# ask 최우선 매도 호가 (매도 주문 중 가장 낮은 가격)
# low 최근 24시간 저가
# high 최고 24시간 고가
# volume 거래량

import requests
import datetime

r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")
# print(r.text) #확인용
bitcoin = r.json()
# print(bitcoin) #확인
# print(type(bitcoin)) #dictype
# print(bitcoin['last']) #최정 체결가격 value값 출력

timestamp = bitcoin['timestamp']
print(timestamp) #최종 체결 시각
date = datetime.datetime.fromtimestamp(timestamp/1000) #date변수에 = .fromtimestamp 사용해서 timestamp 값을 datetime 객체로 변경
print(date)