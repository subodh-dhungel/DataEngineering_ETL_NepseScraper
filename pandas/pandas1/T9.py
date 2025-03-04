# 9. Filter homelessness for cases where the number of individuals is greater than ten thousand, assigning to
# ind_gt_10k

import pandas as pd

homelessness = pd.read_csv("../homelessness.csv")
ind_gt_10k = homelessness[homelessness["individuals"] > 10000]
print(ind_gt_10k)