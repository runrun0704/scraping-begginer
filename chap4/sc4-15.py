import pandas as pd

df = pd.read_csv("消火栓.csv", encoding = "shift_jis")

hydrant = df[["緯度", "経度"]].values
print(len(hydrant))
print(hydrant)