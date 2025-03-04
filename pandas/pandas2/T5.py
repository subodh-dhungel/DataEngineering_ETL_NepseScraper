import pandas as pd

# Read the CSV file
homelessness = pd.read_csv("../outputs/homelessness_modified.csv")

# Drop columns that start with "Unnamed"
homelessness_cleaned = homelessness.loc[:, ~homelessness.columns.str.startswith("Unnamed")]

homelessness_cleaned.to_csv("../outputs/homelessness_modified.csv")
# Print the cleaned DataFrame
print(homelessness_cleaned)