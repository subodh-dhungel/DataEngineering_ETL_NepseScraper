# 5. Sort homelessness first by region (ascending), and then by number of family members (descending).
# Save this as homelessness_reg_fam

import pandas as pd 

df = pd.read_csv("../homelessness.csv")

#sort homelessness by region (ascending) and the number of family members [descending]
homelessness_reg_fam = df.sort_values(by=["region", "family_members"], ascending=[True, False])

#save it to another file
print(homelessness_reg_fam)
homelessness_reg_fam.to_csv("../outputs/homelessness_reg_fam.csv", header="Homelessness by region(ascending) and then by family members(descending)")
