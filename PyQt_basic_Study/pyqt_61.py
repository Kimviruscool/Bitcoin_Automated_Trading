# 기간 수익률이 높은 코인 찾기

import pybithumb
import numpy as np

def get_hpr(ticker) :
    try : #예외처리
        df = pybithumb.get_ohlcv(ticker) #코인정보 가져오기
        df = df['2024'] #조회 년도 지정

        df['ma5'] = df['close'].rolling(window=5).mean().shift(1)  # 종가데이터 5일 이동평균을 계산 shift(1) 을 해서 excel에서 표기시 한행밑으로내려 저장
        df['range'] = (df['high'] - df['low']) * 0.5  # 고가 - 저가 * 0.5 = 차이값 #차이값 컬럼추가
        df['target'] = df['open'] + df['range'].shift(1)  # 목표값 컬럼 추가 = 시가 + 차이값 #한행 내려서 저장
        df['bull'] = df['open'] > df['ma5']  # bull 상승장 컬럼추가 = 거래일의 시가가 전일 종가까지 계산된 5일 이동평균보다 크면 true를 아니면 false를 저장

        fee = 0.0032 # 수수료 지정
        df['ror'] = np.where((df['high'] > df['target']) & df['bull'], df['close'] / df['target'] - fee , 1) #수익률컬럼 추가 numpy 조건사용 (고가가 목표보다 높고 AND bull이 true(상승장)일때 ,(참) 종가 / 목표값 - 수수료 ,거짓 1(현금보유) )

        df['hpr'] = df['ror'].cumprod()  # 기간 수익률, 누적수익률 (HPR) 계산: 일별 수익률(ror)을 모두 곱하여 자산이 어떻게 불어났는지 계산

        df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
        # 낙폭(Drawdown) 계산: (현재까지의 최고 수익률 - 현재 수익률) / 현재까지의 최고 수익률 * 100
        # 설명: 전 고점 대비 현재 자산이 몇 퍼센트 하락했는지를 나타냄

        return df['hpr'][-2] #반환처리 기간 수익률이 최근 2일전까지의
    except Exception as e: #예외처리
        print(f"{ticker} 에러 발생: {e}")
        # 현재 에러 발생
        return 1

tickers = pybithumb.get_tickers() #코인 목록 가져오기

hprs = [] #hprs 기간수익률들의 데이터 리스트 생성

for ticker in tickers : #코인하나씩 시세 조회 반복
    hpr = get_hpr(ticker) #hpr변수에 코인 기간수익률 바인딩
    hprs.append((ticker, hpr)) #(코인이름, 수익률) 튜플로 묶어서 리스트에 저장

# 정렬
# sorted(대상, key=기준, reverse=차순)
# key=lambda x:x[1] : 리스트 안의 데이터 (코인, 수익률) 중 [1]번째인 '수익률'을 기준으로 정렬하라는 뜻
# reverse=True : 내림차순 (큰 숫자부터 작은 숫자 순서로)
sorted_hprs = sorted(hprs, key=lambda x:x[1], reverse=True)

print(sorted_hprs[:5])
# 결과 [('BTC', 1), ('ETH', 1), ('ETC', 1), ('XRP', 1), ('BCH', 1)]
# 해석 : 해당 코인들이 기간수익률이  높음