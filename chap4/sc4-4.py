import pandas as pd

df = pd.read_csv("FEH_00200524_220126144800.csv", index_col = "全国・都道府県", encoding = "shift_jis")

print(len(df))
print(df.columns.values)