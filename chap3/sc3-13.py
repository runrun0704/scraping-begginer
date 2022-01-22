import pandas as pd

df = pd.read_csv("test.csv")

syakai = df.sort_values("社会", ascending = False)

syakai.to_csv("export3.csv", index = False, header = False)