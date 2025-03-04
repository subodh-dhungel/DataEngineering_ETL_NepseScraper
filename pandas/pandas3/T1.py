# Set the index of `temperatures` to `"city"`, assigning to `temperatures_ind`.
# - **Look at `temperatures_ind`. How is it different from `temperatures`?**
# - Reset the index of `temperatures_ind`, keeping its contents.
# - Reset the index of `temperatures_ind`, dropping its contents.

import pandas as pd

df = pd.read_csv("../temperatures.csv")
temperatures_ind = df.set_index("city")

# original dataframe
print("original dataframe")
print(df.head())

# city as index
print("\ndataframe with city as index: ")
print(temperatures_ind.head())

# reset index while keeping "city" as column
reset_keep = temperatures_ind.reset_index()
print("\nReset index (keeping 'city' column): ")
print(reset_keep.head())

# reset index while dropping city column
reset_drop = temperatures_ind.reset_index(drop=True)
print("\nReset index (dropping 'city' column): ")
print(reset_drop.head())

print(temperatures_ind)