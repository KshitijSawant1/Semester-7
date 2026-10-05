import nltk
from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.stem import SnowballStemmer, WordNetLemmatizer

nltk.download("wordnet")

words = ["running", "studies", "cars", "playing", "eating"]

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer("english")
lemma = WordNetLemmatizer()

print("Word\t\tPorter\t\tLancaster\tSnowball\tLemma")

for word in words:
    print(
        word, "\t\t",
        porter.stem(word), "\t\t",
        lancaster.stem(word), "\t\t",
        snowball.stem(word), "\t\t",
        lemma.lemmatize(word)
    )
