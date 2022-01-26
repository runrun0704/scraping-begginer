import pandas as pd

df = pd.read_csv("13TOKYO.CSV", header = None, encoding = "shift_jis")

results = df[df[8] == "東葛西"]
print(results[7])

results = df[df[8].str.contains("東葛西")]
print(results[7])