# 3. Sort homelessness by the number of homeless individuals in the individuals column, from
# smallest to largest, and save this as homelessness_ind. Print the head of the sorted DataFrame.

import pandas as pd

df = pd.read_csv("../homelessness.csv")

# sorting the data and displaying the result
by_nof_indviduals = df.sort_values(ascending=True, by="individuals")
#print(by_nof_indviduals)

# save as homelessness_ind
by_nof_indviduals.to_csv("../outputs/homelessness_ind.csv",header="Homeless by number of Individuals In the US")

# print the header
header = by_nof_indviduals.head(1)
print(header)
