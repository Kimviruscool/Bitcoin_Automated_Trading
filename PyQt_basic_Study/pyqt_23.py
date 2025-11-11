# 예외 처리 #try ~ except

price = {"open" : 100 ,
        "high" : 150,
        "low" : 90,
         "close" : 130}

print("point-1")
# open = price["open1"]
# print("point-2")

# 결과
# open = price["open1"]
#         ~~~~~^^^^^^^^^
# KeyError: 'open1'
# point-1

# 예외처리
try:
    open = price["open1"]
except :
    pass

print("point-2")