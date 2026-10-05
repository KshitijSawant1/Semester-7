# Experiment 1 – Study of Different NLP Tools

## Theory

**Natural Language Processing (NLP)** is a branch of Artificial Intelligence that enables computers to **understand, process, analyze, and generate human language**. NLP combines concepts from computer science, machine learning, and linguistics to process textual and spoken data.

Various NLP tools and libraries are available in Python that simplify common language-processing tasks.

### 1. NLTK (Natural Language Toolkit)

**NLTK** is a widely used Python library for learning and implementing fundamental NLP techniques. It provides functions and datasets for:

- Tokenization
- Stemming
- Lemmatization
- Stop-word removal
- Part-of-Speech (POS) tagging
- Named Entity Recognition
- Text classification

For example, tokenization using NLTK can divide:

**“NLP is interesting.”**

into:

**[“NLP”, “is”, “interesting”, “.”]**

### 2. spaCy

**spaCy** is an efficient NLP library designed for practical and production-oriented applications. It provides pretrained language models that can process text quickly.

It supports:

- Tokenization
- POS tagging
- Lemmatization
- Dependency parsing
- Named Entity Recognition (NER)
- Sentence segmentation

For example, spaCy can identify **“Mumbai”** as a location and **“Google”** as an organization.

### 3. TextBlob

**TextBlob** provides a simple interface for performing common NLP operations. It is especially useful for beginners because many tasks can be performed using very little code.

It supports:

- Sentiment analysis
- Tokenization
- POS tagging
- Text classification
- Basic language processing

In sentiment analysis, TextBlob provides **polarity** to indicate whether a sentence expresses positive, negative, or neutral sentiment.

### Applications of NLP Tools

NLP tools are commonly used in:

- Chatbots and virtual assistants
- Sentiment analysis
- Machine translation
- Search engines
- Spam detection
- Text summarization
- Question answering
- Information extraction

### Advantages

- Reduce the complexity of implementing NLP algorithms.
- Provide ready-to-use language-processing functions.
- Support rapid development of NLP applications.
- Pretrained models reduce the need to build everything from scratch.

### Limitations

- Performance depends on the quality of language models and datasets.
- Some tools require additional computational resources.
- NLP systems may struggle with **ambiguity, sarcasm, context, and regional languages**.

## Conclusion

**Different NLP tools such as NLTK, spaCy, and TextBlob were studied and used to understand their role in performing basic natural language processing tasks.**