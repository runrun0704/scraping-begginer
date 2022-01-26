import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("FEH_00200524_220126144800.csv", index_col = "全国・都道府県", encoding = "shift_jis")

print(df["2019年"])

df["2019年"].plot.bar()
plt.show()