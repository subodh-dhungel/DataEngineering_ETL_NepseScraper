# 11. Filter homelessness for cases where the number of family_members is less than one thousand and the
# region is "Pacific", assigning to fam_lt_1k_pac

import pandas as pd

homelessness = pd.read_csv("../homelessness.csv")
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific")]
print(fam_lt_1k_pac)