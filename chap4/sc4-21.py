import pandas as pd

df = pd.read_csv("店舗.csv")

store = df[["緯度", "経度", "店舗名"]].values
print(store)