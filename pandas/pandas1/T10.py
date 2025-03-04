# 10. Filter homelessness for cases where the USA Census region is "Mountain",
#  assigning to mountain_reg

import pandas as pd

homelessness = pd.read_csv("../homelessness.csv")
mountain = homelessness[homelessness["region"] == "Mountain"]
print(mountain)