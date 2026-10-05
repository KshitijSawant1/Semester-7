from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

documents = [
    "Natural Language Processing is interesting",
    "Machine Learning and NLP are closely related",
    "Natural Language Processing uses Machine Learning"
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

features = vectorizer.get_feature_names_out()

df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=features
)

print("Features:")
print(features)

print("\nTF-IDF Matrix:")
print(df)
