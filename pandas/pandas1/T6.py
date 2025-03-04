# 6. Create a Series called individuals that contains only the individuals column of homelessness.

import pandas as pd

df = pd.read_csv("../homelessness.csv")
homelessness_col = df["individuals"]
print(homelessness_col)