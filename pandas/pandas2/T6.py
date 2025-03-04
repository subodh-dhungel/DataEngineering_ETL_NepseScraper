# 6. Sort high_homelessness by descending indiv_per_10k, assigning to high_homelessness_srt

import pandas as pd

homelessness = pd.read_csv("../outputs/homelessness_modified.csv")
high_homelessness_srt = homelessness.sort_values("indv_per_10k",ascending=False)
print(high_homelessness_srt)