# 8. Create a DataFrame called ind_state that contains the individuals and state columns of homelessness,
# in that order.

import pandas as pd

df = pd.read_csv("../homelessness.csv")
ind_state = df[["individuals","state"]]
print(ind_state)