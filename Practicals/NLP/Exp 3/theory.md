Your **Experiment 3** is mostly correct, but the **Observation and the final Advantages/Limitations/Application section are from a preprocessing experiment**, not TF-IDF. Replace those parts with the following.

## Observations

- The given text documents were successfully converted into **numerical feature vectors using TF-IDF**.
- Each unique term was represented as a separate feature in the TF-IDF matrix.
- Words occurring frequently in a particular document received a **higher importance score**.
- Words appearing across multiple documents generally received comparatively lower importance.
- A TF-IDF value of **0 indicates that the particular term is absent from that document**.
- The experiment demonstrates how textual documents can be transformed into numerical data suitable for machine learning and information retrieval.

## Advantages, Limitations and Applications

| **Advantages**                       | **Limitations**                                | **Applications**       |
| ------------------------------------ | ---------------------------------------------- | ---------------------- |
| Simple and easy to implement         | Does not understand semantic meaning           | Information Retrieval  |
| Identifies important terms           | Ignores word order                             | Search Engines         |
| Reduces importance of common words   | Cannot understand synonyms                     | Document Ranking       |
| Computationally efficient            | Does not capture context                       | Text Classification    |
| Converts text into numerical vectors | Large vocabulary creates large feature vectors | Sentiment Analysis     |
| Useful for machine learning models   | Less powerful than modern embeddings           | Recommendation Systems |

## Procedure

Your current **“Procedure” contains the program output**, so I would also correct that. Use this as the actual procedure:

1. Import `TfidfVectorizer` from Scikit-learn and `pandas`.
2. Define a collection of sample text documents.
3. Create a `TfidfVectorizer` object.
4. Apply `fit_transform()` to generate the TF-IDF matrix.
5. Extract the feature names using `get_feature_names_out()`.
6. Convert the generated matrix into a Pandas DataFrame.
7. Display the features and corresponding TF-IDF values.
8. Observe the importance assigned to different terms.

The block you currently have under **Procedure** should instead be titled **Output**.

## Conclusion

**The TF-IDF based text representation model was successfully implemented to convert textual documents into numerical feature vectors and determine the relative importance of terms in a document collection.**

With these changes, your Experiment 3 structure becomes:

**Aim → Learning Objective → Tools → Theory → Implementation → Procedure → Output → Observations → Advantages/Limitations/Applications → Conclusion.**
