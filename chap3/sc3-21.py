import pandas as pd
import openpyxl

df = pd.read_csv("test.csv")

kokugo = df.sort_values("国語", ascending = False)

kokugo.to_excel("csv_to_excel2.xlsx", index = False, sheet_name = "国語でソート")