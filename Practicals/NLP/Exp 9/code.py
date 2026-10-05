import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")

text = "The quick brown fox jumps over the lazy dog."

# Tokenization and POS Tagging
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)

print("POS Tags:")
print(pos_tags)

# Chunk Grammar
grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>+}
    VP: {<VB.*>}
    PP: {<IN><NP>}
"""

# Chunking
parser = RegexpParser(grammar)
tree = parser.parse(pos_tags)

print("\nChunk Tree:")
print(tree)

print("\nExtracted Chunks:")
for chunk in tree.subtrees():
    if chunk.label() != "S":
        words = " ".join(word for word, tag in chunk.leaves())
        print(chunk.label(), "->", words)
