# Inspecting dataframe
# 1. Print the head, information, number of rows and columns, and description of the homelessness
# data

import pandas as pd

df = pd.read_csv("../homelessness.csv", header=None)

header = df.head()
information =  df.info()
rows = len(df)
columns = len(df.columns)

#print header
print(header)

#print information
print(information)

#print no of rows and columns
print(rows)
print(columns)

#print description of the homelessness data
print(df.describe())