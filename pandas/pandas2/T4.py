# 4. Add a column to homelessness, indiv_per_10k, containing the number of homeless
# individuals per ten thousand people in each state, using state_pop for state population.

import pandas as pd

homelessness = pd.read_csv("../outputs/homelessness_modified.csv")
homelessness["indv_per_10k"] = homelessness["p_homeless"] * 10000
homelessness.to_csv("../outputs/homelessness_modified.csv")
print(homelessness)