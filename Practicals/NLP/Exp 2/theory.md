# Experiment 2

### Aim

**Study Different Applications and Preprocessing Steps in Natural Language Processing.**

## Theory

**Natural Language Processing (NLP)** is a branch of Artificial Intelligence that enables computers to **understand, process, analyze, and generate human language**. Human language is generally unstructured and may contain punctuation, unnecessary words, different word forms, and other variations. Therefore, **text preprocessing** is performed before applying NLP algorithms.

### Applications of NLP

NLP is used in many real-world applications:

- **Sentiment Analysis:** Identifies whether a text expresses positive, negative, or neutral sentiment.
- **Chatbots:** Understands user queries and generates suitable responses.
- **Machine Translation:** Translates text from one language to another.
- **Text Summarization:** Converts lengthy documents into shorter summaries.
- **Spam Detection:** Identifies unwanted or spam messages.
- **Search Engines:** Understands queries and retrieves relevant information.
- **Question Answering:** Automatically answers questions written in natural language.
- **Information Extraction:** Extracts important information such as names, places, and organizations from text.

## NLP Preprocessing Steps

### 1. Lowercase Conversion

All text is converted into lowercase so that words such as **“Language”** and **“language”** are treated as the same word.

### 2. Tokenization

Tokenization divides a sentence into smaller units called **tokens**.

Example:  
**“NLP is useful” → [“NLP”, “is”, “useful”]**

### 3. Punctuation Removal

Symbols such as **. , ! ? ;** are removed when they do not contribute useful information to the NLP task.

### 4. Stop-Word Removal

Frequently occurring words such as **“the”, “is”, “a”, “an”, “and”** can be removed to retain more meaningful words.

### 5. Stemming

Stemming reduces different forms of a word to a common root or stem.

Example:  
**playing, played, plays → play**

### 6. Lemmatization

Lemmatization converts a word into its **meaningful dictionary base form**.

Example:  
**cars → car**  
**better → good**

### Importance of Preprocessing

Text preprocessing helps to:

- Remove unnecessary information.
- Reduce the size of textual data.
- Standardize different forms of words.
- Improve the quality of input given to NLP models.
- Improve the efficiency and accuracy of many NLP applications.

### Conclusion

**Different applications of NLP and preprocessing techniques such as lowercasing, tokenization, punctuation removal, stop-word removal, stemming, and lemmatization were studied and implemented successfully.**
