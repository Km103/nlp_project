from nltk.util import bigrams
from collections import Counter
import nltk
from nltk.probability import FreqDist

def getBiGramProb(tokens):
    # Create bi-grams
    bi_grams = list(bigrams(tokens))

    # Count the frequency of each bi-gram
    bi_gram_counts = Counter(bi_grams)

    # Calculate the total number of bi-grams
    total_bi_grams = len(bi_grams)

    # Calculate bi-gram probabilities
    bi_gram_probabilities = {bi_gram: count / total_bi_grams for bi_gram, count in bi_gram_counts.items()}

    return bi_gram_probabilities
