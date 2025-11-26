# Collum Shift (데이터 프레임 한 줄 올리기,내리기)

from pandas import *

s = Series([100,200,300])
s2 = s.shift(1)
print(s,"\n")
print(s2,"\n")

s = Series([100,200,300])
s2 = s.shift(-1)
print(s,"\n")
print(s2,"\n")