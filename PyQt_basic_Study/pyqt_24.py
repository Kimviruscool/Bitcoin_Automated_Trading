#예외처리 가정하여 에러처리하기

import pybithumb
import time

# while True:
#     price = pybithumb.get_current_price("BTC")
#     print(price/10)
#     time.sleep(0.2)

# # 방법1 if is
# while True:
#     price = pybithumb.get_current_price("BTC")
#     if price is not None:
#         print(price/10)
#     time.sleep(0.2)

# 방법2 try except
while True:
    price = pybithumb.get_current_price("BTC")
    try :
        print(price/10)
    except :
        print("error")
    time.sleep(0.2)