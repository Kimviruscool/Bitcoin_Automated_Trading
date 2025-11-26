# 보안 및 예외처리
# connect key , secret key를 메모장에 저장해  파일열기를 통해 사용

import pybithumb

# 메모장에 저장된 키 읽어오기
with open("C:/Users/0000/Desktop/bithumb.txt") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()
    bithum = pybithumb.Bithumb(key, secret)

# current_price = bithum.get_current_price("BTC")
# if current_price > target_price:
# buy_crypto_currency("BTC")

try :
    if None > 123:
        print("정상")
except :
    print("에러 발생")
