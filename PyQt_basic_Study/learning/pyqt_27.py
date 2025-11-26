#가상화폐별 상승하락장 판단하기

import pybithumb

def bull_market(ticker): #상승하락장 기능 정의
    df = pybithumb.get_ohlcv(ticker) #파라미터 값으로 받아온 ticker(가상화폐분류코드)를 사용해서 코인 조회
    ma5 = df['close'].rolling(window=5).mean() # 코인데이터중 종가를 5개씩 그룹화
    price = pybithumb.get_current_price(ticker) #파라미터값의 코인 가격 저장
    last_ma5 = ma5.iloc[-2] #코인종가 데이터중 마지막에서 두번째 데이터 대입

    if price > last_ma5: #만약 오늘가격이 어제 가격보다 크면 반환 아니면 반환하지 않음
        print(ticker,"상승장")
        return True
    else:
        print(ticker,"하락장")
        return False

# is_bull = bull_market('BTC') #테스트용
