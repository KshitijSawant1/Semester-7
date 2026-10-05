import nltk
import spacy
from textblob import TextBlob

nltk.download("punkt_tab")

text = "Natural Language Processing makes computers understand human language."

print("Original Text:")
print(text)

print("\nNLTK Tokenization:")
print(nltk.word_tokenize(text))

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

print("\nspaCy POS Tagging:")
for token in doc:
    print(token.text, "-", token.pos_)

blob = TextBlob(text)

print("\nTextBlob Sentiment:")
print("Polarity:", blob.sentiment.polarity)
print("Subjectivity:", blob.sentiment.subjectivity)