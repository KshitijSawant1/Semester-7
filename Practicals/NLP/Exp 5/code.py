import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter

nltk.download("punkt_tab")

text = "I love natural language processing and I love to learn NLP"

# Tokenization
tokens = word_tokenize(text.lower())

# Generate N-grams
unigrams = list(ngrams(tokens, 1))
bigrams = list(ngrams(tokens, 2))
trigrams = list(ngrams(tokens, 3))

print("Tokens:", tokens)
print("\nUnigrams:", unigrams)
print("\nBigrams:", bigrams)
print("\nTrigrams:", trigrams)

# Bigram probability P(love | i)
unigram_count = Counter(tokens)
bigram_count = Counter(bigrams)

probability = bigram_count[("i", "love")] / unigram_count["i"]

print("\nP(love | i) =", probability)
