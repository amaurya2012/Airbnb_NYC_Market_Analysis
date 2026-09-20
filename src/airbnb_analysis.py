"""
Airbnb NYC Market Analysis - Complete EDA Script
Dataset: AB_NYC_2019.csv

Expected project structure:
airbnb_nyc_market_analysis/
├── data/AB_NYC_2019.csv
├── outputs/charts/
└── outputs/cleaned_data/
"""

from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "AB_NYC_2019.csv"
CHART_DIR = BASE_DIR / "outputs" / "charts"
CLEAN_DIR = BASE_DIR / "outputs" / "cleaned_data"

CHART_DIR.mkdir(parents=True, exist_ok=True)
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")
pd.set_option("display.max_columns", None)

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"\nDataset not found: {DATA_PATH}\n"
        "Download AB_NYC_2019.csv and place it in the data folder."
    )

df = pd.read_csv(DATA_PATH)

print("=" * 70)
print("AIRBNB NYC MARKET ANALYSIS")
print("=" * 70)
print(f"Original shape: {df.shape}")

# Cleaning
clean_df = df.drop_duplicates().copy()
clean_df["last_review"] = pd.to_datetime(clean_df["last_review"], errors="coerce")
clean_df["reviews_per_month"] = clean_df["reviews_per_month"].fillna(0)
clean_df["host_name"] = clean_df["host_name"].fillna("Unknown")
clean_df["name"] = clean_df["name"].fillna("Unknown Listing")

clean_df = clean_df[
    (clean_df["price"] >= 0) &
    (clean_df["minimum_nights"] >= 1) &
    (clean_df["availability_365"].between(0, 365))
].copy()

clean_df["has_reviews"] = clean_df["number_of_reviews"].fillna(0).gt(0)
clean_df["review_year"] = clean_df["last_review"].dt.year
clean_df["review_month"] = clean_df["last_review"].dt.month
clean_df["price_band"] = pd.cut(
    clean_df["price"],
    bins=[-1, 50, 100, 200, 500, np.inf],
    labels=["$0-50", "$51-100", "$101-200", "$201-500", "$500+"]
)

# Save cleaned data
clean_df.to_csv(CLEAN_DIR / "airbnb_cleaned.csv", index=False)

# 1. Listings by borough
borough_counts = clean_df["neighbourhood_group"].value_counts()
plt.figure(figsize=(9, 5))
sns.barplot(x=borough_counts.index, y=borough_counts.values)
plt.title("Number of Airbnb Listings by Borough")
plt.xlabel("Borough")
plt.ylabel("Number of Listings")
plt.tight_layout()
plt.savefig(CHART_DIR / "listings_by_borough.png", dpi=200)
plt.close()

# 2. Room types
room_counts = clean_df["room_type"].value_counts()
plt.figure(figsize=(8, 5))
sns.barplot(x=room_counts.index, y=room_counts.values)
plt.title("Airbnb Listings by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Number of Listings")
plt.tight_layout()
plt.savefig(CHART_DIR / "room_type_distribution.png", dpi=200)
plt.close()

# 3. Average price
avg_price = (
    clean_df.groupby("neighbourhood_group", as_index=False)["price"]
    .mean()
    .sort_values("price", ascending=False)
)
avg_price.to_csv(CLEAN_DIR / "avg_price_by_borough.csv", index=False)

plt.figure(figsize=(9, 5))
sns.barplot(data=avg_price, x="neighbourhood_group", y="price")
plt.title("Average Airbnb Price by Borough")
plt.xlabel("Borough")
plt.ylabel("Average Price per Night")
plt.tight_layout()
plt.savefig(CHART_DIR / "average_price_by_borough.png", dpi=200)
plt.close()

# 4. Median price by borough and room
median_price = (
    clean_df.groupby(["neighbourhood_group", "room_type"], as_index=False)["price"]
    .median()
)
median_price.to_csv(CLEAN_DIR / "median_price_by_borough_room_type.csv", index=False)

# 5. Top neighborhoods
top_neighborhoods = clean_df["neighbourhood"].value_counts().head(15).sort_values()
plt.figure(figsize=(10, 7))
sns.barplot(x=top_neighborhoods.values, y=top_neighborhoods.index)
plt.title("Top 15 Neighborhoods by Number of Listings")
plt.xlabel("Number of Listings")
plt.ylabel("Neighborhood")
plt.tight_layout()
plt.savefig(CHART_DIR / "top_neighbourhoods.png", dpi=200)
plt.close()

# 6. Price distribution
plt.figure(figsize=(10, 5))
sns.histplot(clean_df["price"], bins=100)
plt.xlim(0, 500)
plt.title("Airbnb Price Distribution (Price <= $500)")
plt.xlabel("Price per Night")
plt.ylabel("Number of Listings")
plt.tight_layout()
plt.savefig(CHART_DIR / "price_distribution.png", dpi=200)
plt.close()

# 7. Geographic plot
geo = clean_df.sample(min(10000, len(clean_df)), random_state=42)
plt.figure(figsize=(10, 8))
sns.scatterplot(
    data=geo,
    x="longitude",
    y="latitude",
    hue="room_type",
    alpha=0.45,
    s=25
)
plt.title("Geographic Distribution of Airbnb Listings")
plt.tight_layout()
plt.savefig(CHART_DIR / "geographic_distribution.png", dpi=200)
plt.close()

# 8. Host analysis
host_summary = (
    clean_df.groupby("host_id")
    .agg(
        listings=("id", "count"),
        total_reviews=("number_of_reviews", "sum"),
        average_price=("price", "mean"),
        average_availability=("availability_365", "mean")
    )
    .sort_values("listings", ascending=False)
)
host_summary.to_csv(CLEAN_DIR / "host_summary.csv")

print(f"Cleaned shape: {clean_df.shape}")
print(f"Average price: ${clean_df['price'].mean():,.2f}")
print(f"Median price: ${clean_df['price'].median():,.2f}")
print(f"Unique hosts: {clean_df['host_id'].nunique():,}")
print(f"Unique neighborhoods: {clean_df['neighbourhood'].nunique():,}")
print(f"Outputs saved in: {CLEAN_DIR}")
print("Analysis completed successfully.")