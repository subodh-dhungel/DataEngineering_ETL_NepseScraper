# 2. Print a 2D NumPy array of the values in homelessness. Print the column names of homelessness.Print the
# index of homelessness

import pandas as pd

df = pd.read_csv("../homelessness.csv")

# Old Method
# array = df.to_numpy()

# New Method
array = df.values

print(array)