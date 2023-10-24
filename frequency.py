import nltk
from nltk.probability import FreqDist
#nltk.download('punkt')
def freq(text):
    #tokenise the text
    book_tokens = nltk.word_tokenize(text)
    # Create a frequency distribution
    fdist = FreqDist(book_tokens)
    # Print the most common tokens and their frequencies
    book_tokens = fdist.most_common(1000)

    return book_tokens
