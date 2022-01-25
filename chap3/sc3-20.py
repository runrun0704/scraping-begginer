import pandas as pd
import openpyxl

df = pd.read_csv("test.csv")

kokugo = df.sort_values("国語", ascending = False)

kokugo.to_excel("csv_to_execel1.xlsx")