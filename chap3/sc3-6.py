import pandas as pd

df = pd.read_csv("test.csv")

df2 = df.drop("名前", axis = 1)

df3 = df2.drop(2, axis = 0)

print(df3)