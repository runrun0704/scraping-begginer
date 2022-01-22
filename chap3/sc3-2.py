import pandas as pd

df = pd.read_csv("test.csv")

print(len(df))
print(df.columns.values)
print(df.index.values)