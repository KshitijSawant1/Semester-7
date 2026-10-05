from gensim.models import Word2Vec

sentences = [
    ["natural", "language", "processing"],
    ["machine", "learning", "is", "interesting"],
    ["natural", "language", "understanding"],
    ["deep", "learning", "for", "nlp"],
    ["nlp", "uses", "machine", "learning"],
    ["language", "models", "process", "text"]
]

# Train Word2Vec model
model = Word2Vec(
    sentences,
    vector_size=20,
    window=3,
    min_count=1,
    sg=0
)

print("Vocabulary:")
print(model.wv.index_to_key)

print("\nVector for 'language':")
print(model.wv["language"])

print("\nWords similar to 'language':")
print(model.wv.most_similar("language", topn=3))
