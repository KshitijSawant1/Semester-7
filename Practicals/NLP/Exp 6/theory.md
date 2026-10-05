Theory
Stemming and Lemmatization are NLP preprocessing techniques used to reduce different forms of words to a common base form. They help reduce vocabulary size and improve text processing.
Stemming
Stemming removes prefixes or suffixes from words using predefined rules. The resulting stem may not always be a valid dictionary word.
Examples:

- playing → play
- studies → studi
- running → run
  Common stemming algorithms include:
- Porter Stemmer – simple and commonly used.
- Lancaster Stemmer – more aggressive in removing word endings.
- Snowball Stemmer – improved version of Porter with support for multiple languages.
  Lemmatization
  Lemmatization converts a word into its meaningful dictionary base form called a lemma. It uses vocabulary and grammatical information rather than simply removing characters.
  Examples:
- cars → car
- studies → study
- running → run when treated as a verb
- better → good when appropriate grammatical information is provided
  Stemming vs Lemmatization
  Stemming Lemmatization
  Uses word-chopping rules Uses vocabulary and grammar
  May generate invalid words Produces meaningful base forms
  Faster Comparatively slower
  Less accurate More linguistically accurate
  Example: studies → studi Example: studies → study

Applications
Both techniques are useful in:

- Search Engines
- Information Retrieval
- Text Classification
- Sentiment Analysis
- Chatbots
- Question Answering
  Observation
  Different stemming algorithms produced different root forms for the same words. Porter, Lancaster, and Snowball reduced words using different stemming rules, while WordNet Lemmatizer generated dictionary-based base forms. This demonstrates that stemming is faster and more aggressive, whereas lemmatization aims to preserve linguistic meaning.
  Conclusion
  Stemming and Lemmatization were successfully implemented and compared. Stemming reduces words using rule-based chopping, while Lemmatization produces more meaningful dictionary base forms.
