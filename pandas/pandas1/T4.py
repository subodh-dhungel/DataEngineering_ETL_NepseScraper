# 4. Sort homelessness by the number of homeless family_members in descending order, and save this as
# homelessness_fam

import pandas as pd

df = pd.read_csv("../homelessness.csv")

#sorting by numbers of homeless family members in descending order
homelessness_fam = df.sort_values("family_members", ascending=False)

# save the data
homelessness_fam.to_csv("../outputs/homelessness_fam.csv")
print(homelessness_fam)
