import spacy

nlp = spacy.load("en_core_web_sm")

text = "John Smith works at Microsoft in Mumbai on Monday."
doc = nlp(text)

# POS Tagging
print("POS Tagging:")
for token in doc:
    print(token.text, "->", token.pos_)

# Named Entity Recognition
print("\nNamed Entities:")
for entity in doc.ents:
    print(entity.text, "->", entity.label_)
