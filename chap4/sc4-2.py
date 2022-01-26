import pandas as pd

df = pd.read_csv("13TOKYO.CSV", header = None, encoding = "shift_jis")

results = df[df[2] == 1340084]
print(results[[2,6,7,8]])