# DataFrame index / slice

import pandas as pd

data = {"open" : [730,750], "high" : [755,780], "low":[700,100], "close":[750,770]}
df = pd.DataFrame(data, index=["2018-01-01", "2018-01-02"])
print(df, "\n\n\n")

print(df.loc["2018-01-01"],"\n")
print(df.iloc[0],"\n")

target = [0, 1]
print(df.iloc[target])

