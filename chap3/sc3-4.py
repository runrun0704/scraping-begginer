import pandas as pd

df = pd.read_csv("test.csv")

print(df.loc[3])

print(df.loc[[0,2]])

print(df.loc[5]["社会"])