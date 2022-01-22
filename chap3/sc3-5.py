import pandas as pd

df = pd.read_csv("test.csv")

df["美術"] = [70, 78, 56, 80, 98, 38]
print(df)

df.loc[6] = ["G惠", 92, 85, 93, 89, 92, 93]
print(df)