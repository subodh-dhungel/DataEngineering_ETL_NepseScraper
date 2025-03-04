# 2. Add a new column to homelessness, named total, containing the sum of the individuals
# and family_members columns.

import pandas as pd

homelessness = pd.read_csv("../homelessness.csv")
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]
homelessness.to_csv("../outputs/homelessness_modified.csv")
print(homelessness)