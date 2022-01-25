import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("test.csv", index_col = 0)

df.T.plot.bar()
plt.legend(loc = "lower right")
plt.savefig("bargraph.png")