from nltk.util import bigrams
from collections import Counter
import nltk
from nltk.probability import FreqDist
import random


def generate_bigrams(tokens):
    # Create bi-grams 
    bi_grams = list(bigrams(tokens))
    return bi_grams


def generate_freq(tokens):
    # Count the frequency of each bi-gram
    freq = FreqDist(tokens)
    return dict(freq)



def create_distinct_tokens(tokens):

    # Create a list of distinct tokens (unique words)
    distinct_tokens = list(set(tokens))

    # Convert the list of distinct tokens back to a regular list (optional)
    distinct_tokens = list(distinct_tokens)
    return distinct_tokens


def find1(s,dct1):
    try:
        return dct1[s]
    except:
        return 0
    

def probability_table(distinct_tokens,dct,dct1):
    n=len(distinct_tokens)
    l=[[]*n for i in range(n)]
    for i in range(n):
        denominator = dct[distinct_tokens[i]]
        for j in range(n):
            numerator = find1(distinct_tokens[i]+" "+distinct_tokens[j],dct1)
            l[i].append(float("{:.3f}".format(numerator/denominator)))
    return l



def getBiGramProb(tokens):

    bigrams=generate_bigrams(tokens)
    dct1=generate_freq(bigrams)
    dct=generate_freq(tokens)
    distinct_tokens=create_distinct_tokens(tokens)
    bi_gram_probabilities=probability_table(distinct_tokens,dct,dct1)
    return bi_gram_probabilities


def PrintTable(bi_gram_probabilities,tokens):

    # for bigram, probability in bi_gram_probabilities:
    #     print(f"{bigram[0]} -> {bigram[1]:<10} Probability: {probability:.2f}")
    distinct_tokens=create_distinct_tokens(tokens)
    n=len(distinct_tokens)
    print("table")
    randomList = random.sample(range(0, len(distinct_tokens)), 10)
    for i in randomList:
        print(distinct_tokens[i], end = "\t")
    print("\n")
    for i in randomList:
        print(distinct_tokens[i], end = "\t")
        for j in randomList:
            print(bi_gram_probabilities[i][j], end = "\t")
        print("\n")



    