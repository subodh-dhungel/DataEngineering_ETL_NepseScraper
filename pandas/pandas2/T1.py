# 1. Filter homelessness for cases where the USA census state is in the list of Mojave states,
# canu, assigning to mojave_homelessness. View the printed result.

import pandas as pd

homelessness = pd.read_csv("../homelessness.csv")
mojave_states = ["California", "Nevada", "Arizona", "Utah"]
mojave_homelessness = homelessness[homelessness["state"].isin(mojave_states)]
print(mojave_homelessness)
