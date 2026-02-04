import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (make sure Data.csv is in the same folder)
df = pd.read_csv("Data.csv")

# ===============================
# 1. Top 10 Cities by Restaurants
# ===============================
city_counts = df["City"].value_counts().head(10)

plt.figure()
city_counts.plot(kind="bar")
plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ===============================
# 2. Distribution of Ratings
# ===============================
plt.figure()
plt.hist(df["Aggregate rating"], bins=20)
plt.title("Distribution of Aggregate Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ===============================
# 3. Cost vs Rating
# ===============================
plt.figure()
plt.scatter(df["Average Cost for two"], df["Aggregate rating"])
plt.title("Average Cost for Two vs Aggregate Rating")
plt.xlabel("Average Cost for Two")
plt.ylabel("Aggregate Rating")
plt.tight_layout()
plt.show()

# ===============================
# 4. Price Range Count
# ===============================
price_counts = df["Price range"].value_counts().sort_index()

plt.figure()
price_counts.plot(kind="bar")
plt.title("Restaurant Count by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()

# ===============================
# 5. Heatmap: Rating vs Price Range
# ===============================
plt.figure()
sns.countplot(x="Price range", hue="Rating text", data=df)
plt.title("Rating Distribution Across Price Ranges")
plt.xlabel("Price Range")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
