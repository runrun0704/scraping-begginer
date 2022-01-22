import pandas as pd

df = pd.read_csv("test.csv")

data_s = df[df["国語"] > 90]
print(data_s)

data_c = df[df["数学"] < 70]
print(data_c["数学"])