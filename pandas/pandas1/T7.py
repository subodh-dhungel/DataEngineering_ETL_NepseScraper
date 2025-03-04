# 7. Create a DataFrame called state_fam that contains only the state and family_members columns of
# homelessness, in that order.

import pandas as pd

df = pd.read_csv("../homelessness.csv")
state_fam = df[["state","family_members"]]
print(state_fam)