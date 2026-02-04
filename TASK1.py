import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: URL of the website
url = "https://quotes.toscrape.com"

# Step 2: Send HTTP request
response = requests.get(url)

# Step 3: Check response status
if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

# Step 4: Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Step 5: Extract required data
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
tags_list = soup.find_all("div", class_="tags")

data = []

for quote, author, tags in zip(quotes, authors, tags_list):
    tag_text = [tag.text for tag in tags.find_all("a", class_="tag")]

    data.append({
        "Quote": quote.text,
        "Author": author.text,
        "Tags": ", ".join(tag_text)
    })

# Step 6: Convert to DataFrame
df = pd.DataFrame(data)

# Step 7: Save to CSV file
df.to_csv("quotes_dataset.csv", index=False, encoding="utf-8")

print("Web scraping completed successfully!")
print(df.head())
