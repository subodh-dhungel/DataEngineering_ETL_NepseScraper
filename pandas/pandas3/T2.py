# Create a list called `cities` that contains "Moscow" and "Saint Petersburg".
# - Use `[]` subsetting to filter `temperatures` for rows where the `city` column takes a value in the
# `cities` list.
# - Use `.loc[]` subsetting to filter `temperatures_ind` for rows where the city is in the `cities` list.

import pandas as pd

df = pd.read_csv("../temperatures.csv")
