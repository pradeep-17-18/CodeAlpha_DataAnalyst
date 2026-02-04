import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("quotes_dataset.csv")

print("Dataset loaded successfully!\n")

# Step 2: Ask meaningful questions
print("Key Questions Before Analysis:")
print("1. How many quotes are there?")
print("2. Who are the most frequent authors?")
print("3. What are the most common tags?")
print("4. Are there missing values?")
print("5. Are there unusual or duplicate records?\n")

# Step 3: Understand data structure
print("Dataset Info:")
print(df.info(), "\n")

print("First 5 Records:")
print(df.head(), "\n")

print("Dataset Shape (Rows, Columns):")
print(df.shape, "\n")

# Step 4: Check missing values
print("Missing Values:")
print(df.isnull().sum(), "\n")

# Step 5: Check duplicates
duplicate_count = df.duplicated().sum()
print(f"Duplicate rows found: {duplicate_count}\n")

# Step 6: Feature Engineering
df["Quote_Length"] = df["Quote"].apply(len)

# Step 7: Statistical summary
print("Statistical Summary:")
print(df["Quote_Length"].describe(), "\n")

# Step 8: Identify trends & patterns

# Top authors
top_authors = df["Author"].value_counts().head(10)

plt.figure()
top_authors.plot(kind="bar")
plt.title("Top 10 Authors by Number of Quotes")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Quote length distribution
plt.figure()
sns.histplot(df["Quote_Length"], bins=20)
plt.title("Distribution of Quote Lengths")
plt.xlabel("Quote Length")
plt.ylabel("Frequency")
plt.show()

# Step 9: Analyze tags
all_tags = df["Tags"].str.split(", ").explode()
top_tags = all_tags.value_counts().head(10)

plt.figure()
top_tags.plot(kind="bar")
plt.title("Top 10 Most Common Tags")
plt.xlabel("Tag")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 10: Detect anomalies
long_quotes = df[df["Quote_Length"] > df["Quote_Length"].mean() + 2*df["Quote_Length"].std()]
print("Potential Anomalies (Very Long Quotes):")
print(long_quotes[["Quote", "Author", "Quote_Length"]].head())

print("\nEDA completed successfully!")
