import pandas as pd

df1 = pd.read_csv("平均気温.csv", index_col = "時点")
df2 = pd.read_csv("最高気温.csv", index_col = "時点")
df3 = pd.read_csv("最低気温.csv", index_col = "時点")

print(df1.columns.values)