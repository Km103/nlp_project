import nltk
from nltk.probability import FreqDist
nltk.download('punkt')

def createToken(text):
# Tokenize the text
    tokens = nltk.word_tokenize(text)

    return tokens