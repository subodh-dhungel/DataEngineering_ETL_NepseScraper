import pandas as pd

df = pd.read_csv("/home/subodh/workingDirectory/internship/pandas/Google-Shopping-dataset-sample.csv", encoding="utf-8")

#*******************************************************************************************
#****************************** Cleaning the data ******************************************
#*******************************************************************************************
df.columns = df.columns.str.lower()

if df.isnull().values.any():
    df.fillna({col: "Not Available" for col in df.select_dtypes(include=["object"]).columns}, inplace=True)
    df.fillna(0, inplace=True)
    obj_cols = df.select_dtypes(include=["object"]).columns
    df[obj_cols] = df[obj_cols].map(lambda x: [] if x == "[]" else x)
    print("Missing values have been replaced")
else:
    print("No missing values were found")

columns_to_drop = [
    "url", "images", "product_id", "return_policy", "product_specifications", 
    "related_items", "product_description", "product_details", "variations", 
    "amount_of_stars"
]
df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)
df["condition"] = "new"
if "item_price" in df.columns:
    df["item_price"] = df["item_price"].astype(str).str.lower().fillna("")
    df.loc[df["item_price"].str.contains(r"\bused\b", na=False, regex=True), "condition"] = "used"
    df.loc[df["item_price"].str.contains(r"\brefurbished\b", na=False, regex=True), "condition"] = "refurbished"
    df.drop(columns=["item_price"], inplace=True)

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
        return "Other - Not Available"
    
    for category, keywords in categories.items():
        if any(keyword in title for keyword in keywords) or any(tag in tags for tag in keywords):
            return category

    return "other"

df["category"] = df.apply(categorize_product, axis=1)

#********************************************************************************************
#******************** Handling Prices: Highest & Lowest for New Products ********************
#********************************************************************************************

if "total_price" in df.columns:
    df["total_price"] = df["total_price"].replace({r"[\$,]": ""}, regex=True).astype(float)
    df["total_price"] = pd.to_numeric(df["total_price"])

    df_new = df[df["condition"] == "new"].dropna(subset=["total_price"])

    highest_prices = df_new.groupby("category")["total_price"].max()
    lowest_prices = df_new.groupby("category")["total_price"].min()

    print("\n********** Highest and Lowest Prices (New Only) **********")
    for category in highest_prices.index:
        print(f"Category: {category}")
        print(f"Highest Price: {highest_prices[category]:.2f}")
        print(f"Lowest Price: {lowest_prices[category]:.2f}")
        print("-" * 30)
else:
    print("\nNo 'total_price' column found in dataset.")

#********************************************************************************************
#********************** Sales Analysis: Top Sales, Top Seller, Most Rated *******************
#********************************************************************************************

def extract_brand(title):
    words = title.split()
    if len(words) > 1:
        return words[0]  
    return "Unknown"

df["brand"] = df["title"].apply(lambda x: extract_brand(str(x).lower()))

top_selling_brands = df["brand"].value_counts().head(10)

print("\n********** Top 10 Selling Brands **********")
print(top_selling_brands)

if "reviews_count" in df.columns and "rating" in df.columns:
    df["reviews_count"] = pd.to_numeric(df["reviews_count"], errors="coerce").fillna(0)
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce").fillna(0)

    most_rated_product = df.loc[df["reviews_count"].idxmax(), ["title", "reviews_count"]]

    highest_rated_product = df.loc[df["rating"].idxmax(), ["title", "rating"]]

    print("\n********** Most Rated Product **********")
    print(f"Product: {most_rated_product['title']}")
    print(f"Reviews Count: {most_rated_product['reviews_count']}")

    print("\n********** Highest Rated Product **********")
    print(f"Product: {highest_rated_product['title']}")
    print(f"Rating: {highest_rated_product['rating']:.2f}")

    # ********************************************************************************************
    # ******************************* Highest Rated Product Per Category *************************
    # ********************************************************************************************

    highest_rated_per_category = df.loc[df.groupby("category")["rating"].idxmax(), ["category", "title", "rating"]]

    print("\n********** Highest Rated Products Per Category **********")
    for _, row in highest_rated_per_category.iterrows():
        print(f"Category: {row['category']}")
        print(f"Highest Rated Product: {row['title']}")
        print(f"Rating: {row['rating']:.2f}")
        print("-" * 30)
else:
    print("\nNo 'reviews_count' or 'rating' column found in dataset.")
