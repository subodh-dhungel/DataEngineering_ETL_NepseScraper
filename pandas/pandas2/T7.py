# 7. Select only the state and indiv_per_10k columns of high_homelessness_srt and save as
# result. Look at the result

import pandas as pd

homelessness = pd.read_csv("../outputs/homelessness_modified.csv")
high_homelessness_srt = homelessness[["state","indv_per_10k"]].sort_values("indv_per_10k", ascending=False)
high_homelessness_srt.to_csv("../outputs/result.csv")
print(high_homelessness_srt)