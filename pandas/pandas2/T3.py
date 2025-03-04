# 3.Add another column to homelessness, named p_homeless, containing the proportion of the
# total homeless population to the total population in each state state_pop.

import pandas as pd

homelessness = pd.read_csv("../outputs/homelessness_modified.csv")
homelessness["p_homeless"] = (homelessness["total"] / homelessness["state_pop"]) * 100
homelessness.to_csv("../outputs/homelessness_modified.csv")
print(homelessness)