import pandas as pd

df = pd.read_csv("/home/subodh/workingDirectory/internship/pandas/GoogleDatasetEdited.csv")

unusefulCol = ["product_id", "variations", "return_policy", "related_items", "images", "product_specifications"]
df.drop(columns=unusefulCol, axis=1, inplace=True)

df["total_price"] = df["total_price"].astype(str)

# Regular expressions for different currencies
currency_patterns = {
    "USD": r"(\$)",  # Capture the dollar symbol
    "EUR": r"(€)",   # Capture the euro symbol
    "AED": r"(AED)", # Capture AED
    "RM": r"(RM)",   # Capture RM
    "AD": r"(AD)"    # Capture AD
}

# Create a new column for currency, initialized to None
df["currency"] = None

# Loop through each currency pattern and assign it
for currency, pattern in currency_patterns.items():
    # Extract the currency symbol and directly assign it to the 'currency' column
    df.loc[df["total_price"].str.contains(pattern, regex=True), "currency"] = currency

# Check for rows where the currency column is still None, indicating no match
print("Rows without a matched currency:")
print(df[df["currency"].isna()])

if df["total_price"].str.contains(r"[\$€A-Za-z,\s]*([\d,.]+)\s*-\s*[\$€A-Za-z,\s]*([\d,.]+)").any():
    print("the column contains the regex")
    df[["price_from", "price_to"]] = df["total_price"].str.extract(r"[\$€A-Za-z,\s]*([\d,.]+)\s*-\s*[\$€A-Za-z,\s]*([\d,.]+)")
    df["price_from"] = df["price_from"].astype(str).str.replace(",", "").astype(float)
    df["price_to"] = df["price_to"].astype(str).str.replace(",", "").astype(float)

if df["item_price"].str.contains(r"[\$€₹,.\d]+").any():
    df[["price_from", "price_to"]] = df["item_price"].str.extract(r"\$?([\d,.\s]+)\$?([\d,.\s]*)", expand=True)
    df["price_from"] = df["price_from"].str.replace(r"[^\d.]", "", regex=True)
    df["price_to"] = df["price_to"].str.replace(r"[^\d.]", "", regex=True)
    df["price_from"] = pd.to_numeric(df["price_from"], errors="coerce")
    df["price_to"] = pd.to_numeric(df["price_to"], errors="coerce")
    df["price_from"].fillna(df["price_to"], inplace=True)
    df["price_to"] = df["price_to"].where(df["price_to"].notna(), None)

# Clean the total_price column
df["total_price"] = df["total_price"].str.replace(r"[^\d.,]", "", regex=True)
df["total_price"] = df["total_price"].str.replace(r"\.(?=.*\.)", "", regex=True)  # Remove extra decimals
df["total_price"] = df["total_price"].str.replace(",", "")

# Convert to numeric
df["total_price"] = pd.to_numeric(df["total_price"], errors="coerce")

# Fill empty price_from and price_to with total_price if not present
df["price_from"].fillna(df["total_price"], inplace=True)
df["price_to"].fillna(df["total_price"], inplace=True)

# Save the cleaned dataframe
df.to_csv("/home/subodh/workingDirectory/internship/pandas/CleanedDataset.csv", index=False)
