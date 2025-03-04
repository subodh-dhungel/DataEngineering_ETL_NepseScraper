import pandas as pd
import os

# Reading different files
df = pd.read_csv("../Google-Shopping-dataset-sample.csv", encoding="utf-8")

#*******************************************************************************************
#******************************Cleaning the data********************************************
#*******************************************************************************************

if df.isnull().values.any():
    print("Missing Values Found")
    print(df.dtypes)

    # Missing values
    df.fillna({col: "Not Available" for col in df.select_dtypes(include=["object"]).columns}, inplace=True)

    # Missing values of numbers
    df.fillna(0, inplace=True)

    # Missing values of empty lists
    obj_cols = df.select_dtypes(include=["object"]).columns
    df[obj_cols] = df[obj_cols].map(lambda x: [] if x == "[]" else x)
    
    print("Missing values have been replaced")
else:
    print("No missing values were found")

# Removing unuseful rows
df.drop(["url", "images", "product_id", "return_policy", "product_specifications", "related_items", 
         "product_description", "product_details", "variations", "amount_of_stars"], axis=1, inplace=True, errors="ignore")

# Filter refurbished, New, Used
df["item_price"] = df["item_price"].astype(str).str.lower().fillna("")

df["condition"] = "new"
df.loc[df["item_price"].str.contains(r"\bused\b", na=False, regex=True), "condition"] = "used"
df.loc[df["item_price"].str.contains(r"\brefurbished\b", na=False, regex=True), "condition"] = "refurbished"
df.drop(columns=["item_price"], inplace=True)

# Adding the category of the items
def categorize_product(row):
    title = row["title"].lower() if isinstance(row["title"], str) else ""
    tags = [tag.lower() for tag in row["tags"]] if isinstance(row["tags"], list) else []

    categories = {
        "laptop": ["laptop", "notebook", "macbook"],
        "smartphone": ["phone", "smartphone", "mobile", "iphone", "dual sim", "5g"],
        "footwear": ["shoes", "sneakers", "footwear", "boots"],
        "clothing": ["shirt", "jeans", "jacket", "clothing"],
        "appliance": ["fridge", "refrigerator", "microwave", "appliance"],
        "tablet": ["tablet", "ipad", "android tablet", "surface", "windows tablet"],
        "playstation": ["playstation", "ps5", "ps4", "console", "nintendo"],
        "oil": ["oil", "vegetable oil", "cooking oil", "sunflower oil"]
    }

    if "not available" in tags:
        for category, keywords in categories.items():
            if any(keyword in title for keyword in keywords) or any(tag in tags for tag in keywords):
                return f"{category} - Not Available"
        return "other"
    
    for category, keywords in categories.items():
        if any(keyword in title for keyword in keywords) or any(tag in tags for tag in keywords):
            return category

    return "other"


df["category"] = df.apply(categorize_product, axis=1)

# Splitting the file by category of item
output_dir = "../categorizedItems"
os.makedirs(output_dir, exist_ok=True)

# Group by category and save each category into its own file
for category, group in df.groupby("category"):
    file_path = os.path.join(output_dir, f"{category}.csv")
    group.to_csv(file_path, index=False)

df.to_csv("../cleanedGoogleDS.csv")

#********************************************************************************************
#********************************Highest and lowest prices***********************************
#********************************************************************************************

def get_highest_and_lowest_prices(category):
    file_path = f"../categorizedItems/{category}.csv"
    if not os.path.exists(file_path):
        print(f"File for {category} not found.")
        return None, None
    
    category_df = pd.read_csv(file_path, encoding="utf-8")
    
    # Filter for new condition only
    category_df = category_df[category_df['condition'] == 'new']
    
    category_df['total_price'] = category_df['total_price'].replace({r'\$': '', ',': ''}, regex=True)
    category_df['total_price'] = pd.to_numeric(category_df['total_price'], errors='coerce')
    
    highest_price = category_df['total_price'].max()
    lowest_price = category_df['total_price'].min()
    
    return highest_price, lowest_price
 
categories = [
    "smartphone", "laptop", "footwear", "clothing", "appliance", 
    "tablet", "playstation", "oil"
]

for category in categories:
    highest, lowest = get_highest_and_lowest_prices(category)
    if highest is not None and lowest is not None:
        print(f"Category: {category.capitalize()}")
        print(f"Highest Price: {highest}")
        print(f"Lowest Price: {lowest}")
        print("-" * 30)
    else:
        print(f"No data available for category: {category}")


