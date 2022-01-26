import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df1 = pd.read_csv("平均気温.csv", index_col = "時点")

df1["東京都"].plot()
plt.ylim(-10, 40)
plt.show()