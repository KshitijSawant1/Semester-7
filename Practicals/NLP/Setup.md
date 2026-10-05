## NLP Practical Setup – Concise Steps

Use **Python 3.13** for Experiments 1–9.

### macOS

```bash
# Install Python 3.13 if required
brew install python@3.13

# Go to project folder
cd "/Users/horizon/Programs/Semester 7"

# Create environment
python3.13 -m venv .venv

# Activate
source .venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install libraries
pip install nltk spacy textblob scikit-learn pandas gensim

# Install spaCy English model
python -m spacy download en_core_web_sm
```

Run an experiment:

```bash
python "Practicals/NLP/Exp 1/code.py"
```

Test all experiments:

```bash
python "Practicals/NLP/test_nlp.py"
```

---

## Windows

```bat
:: Go to project folder
cd "C:\Semester 7"

:: Create environment using Python 3.13
py -3.13 -m venv .venv

:: Activate
.venv\Scripts\activate

:: Upgrade pip
python -m pip install --upgrade pip

:: Install libraries
pip install nltk spacy textblob scikit-learn pandas gensim

:: Install spaCy English model
python -m spacy download en_core_web_sm
```

Run an experiment:

```bat
python "Practicals\NLP\Exp 1\code.py"
```

Test all experiments:

```bat
python "Practicals\NLP\test_nlp.py"
```

### For Future Use

You **do not reinstall the libraries**. Just activate the environment.

**macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```bat
.venv\Scripts\activate
```

To exit the environment:

```bash
deactivate
```
