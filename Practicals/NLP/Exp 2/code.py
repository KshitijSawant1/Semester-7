import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("punkt_tab")
nltk.download("stopwords")

text = "Natural Language Processing is very useful for understanding human languages!"

# Lowercase
text = text.lower()
print("Lowercase:", text)

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Remove punctuation
tokens = [word for word in tokens if word.isalpha()]
print("Without Punctuation:", tokens)

# Remove stopwords
stop_words = set(stopwords.words("english"))
filtered = [word for word in tokens if word not in stop_words]
print("Without Stopwords:", filtered)

# Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in filtered]
print("Stemmed Words:", stemmed)
