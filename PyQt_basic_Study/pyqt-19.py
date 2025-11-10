# DataFrame insert

from pandas import *
import pandas as pd

data = {"open" : [730,750], "high" : [755,780], "low":[700,100], "close":[750,770]}
df = pd.DataFrame(data)
s = Series([300,400])
df["volume"] = s
print(df)

upper = df["open"] * 1.3
df["upper"] = upper