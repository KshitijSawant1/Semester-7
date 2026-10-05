import spacy

nlp = spacy.load("en_core_web_sm")

text = "The children were playing in the gardens."
doc = nlp(text)

print("Morphological Analysis:")
for token in doc:
    print(token.text, "->", token.lemma_, "|", token.morph)

print("\nInflectional Morphology:")
print("cat + s =", "cats")
print("play + ed =", "played")
print("run + ing =", "running")

print("\nDerivational Morphology:")
print("teach + er =", "teacher")
print("happy + ness =", "happiness")
print("un + kind =", "unkind")

print("\nMorpheme Separation:")
print("unbelievable = un + believe + able")
print("happiness = happy + ness")
print("teacher = teach + er")
