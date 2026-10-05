## Theory

### Word Embedding

**Word Embedding** is an NLP technique used to represent words as **dense numerical vectors**. Unlike BoW and TF-IDF, embeddings can capture **semantic and syntactic relationships** between words. Words with similar meanings usually have similar vector representations.

### Word2Vec

**Word2Vec** is a neural-network-based word embedding technique that learns word representations by analyzing the **context in which words occur**. After training, each word is represented by a numerical vector.

### Types of Word2Vec

**1. CBOW (Continuous Bag of Words)**

- Predicts a target word from its surrounding words.
- Faster and computationally efficient.
- Performs well for frequently occurring words.

**2. Skip-Gram**

- Predicts surrounding words from a target word.
- Performs better for rare words.
- Requires more training time than CBOW.

### Advantages

- Captures semantic relationships between words.
- Produces compact, dense vectors.
- Supports word similarity analysis.
- Useful for various NLP models.

### Limitations

- Requires sufficient training data.
- Generates only one vector for each word.
- Cannot properly handle multiple meanings of the same word.
- Does not directly represent complete sentence meaning.

### Applications

- Sentiment Analysis
- Text Classification
- Machine Translation
- Information Retrieval
- Recommendation Systems
- Question Answering

### Conclusion

**Word2Vec converts words into dense numerical vectors and captures relationships between words using CBOW or Skip-Gram models.**
