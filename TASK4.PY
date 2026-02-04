import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from textblob import TextBlob

# Download required NLP resources
nltk.download('punkt')

# Load dataset
df = pd.read_csv("reviews.csv")

# Sentiment Classification
def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["review"].apply(get_sentiment)

# Emotion Detection
def detect_emotion(text):
    text = text.lower()
    if any(word in text for word in ["love", "amazing", "excellent", "great"]):
        return "Happy"
    elif any(word in text for word in ["bad", "worst", "terrible", "hate"]):
        return "Angry"
    else:
        return "Neutral"

df["Emotion"] = df["review"].apply(detect_emotion)

# Sentiment Distribution
plt.figure()
sns.countplot(x="Sentiment", data=df)
plt.title("Sentiment Distribution")
plt.show()

# Emotion Distribution
plt.figure()
sns.countplot(x="Emotion", data=df)
plt.title("Emotion Distribution")
plt.show()

print(df)
