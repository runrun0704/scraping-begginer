import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df1 = pd.read_csv("平均気温.csv", index_col = "時点")
df2 = pd.read_csv("最高気温.csv", index_col = "時点")
df3 = pd.read_csv("最低気温.csv", index_col = "時点")

df1["東京都"].plot()
df2["東京都"].plot()
df3["東京都"].plot()

plt.ylim(-10, 40)
plt.legend(loc = "lower right")
plt.show()