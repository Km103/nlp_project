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
    #print(dict (freq))

    # changing list to dictionary
    return dict(freq)



def create_distinct_tokens(tokens):

    # Create a list of distinct tokens by storing it in the tokens
    distinct_tokens = list(set(tokens))

    # Convert the list of distinct tokens back to a regular list
    distinct_tokens = list(distinct_tokens)
    return distinct_tokens


# find the key s in dictionary dct1
def find1(s,dct1):
    try:
        return dct1[s]
    except:
        return 0
    

def probability_table(distinct_tokens,dct,dct1):
    n=len(distinct_tokens)
    # list to store probabilities
    l=[[]*n for i in range(n)]
    for i in range(n):
        denominator = dct[distinct_tokens[i]]
        for j in range(n):
            #print(distinct_tokens[i]+" "+distinct_tokens[j])

            # finds 2 consective tokens in the bigram dictionary 
            numerator = find1((distinct_tokens[i],distinct_tokens[j]),dct1)
            l[i].append(float("{:.3f}".format(numerator/denominator)))
    return l



def getBiGramProb(tokens):

    bigrams=generate_bigrams(tokens)
    dct1=generate_freq(bigrams)
    dct=generate_freq(tokens)
    distinct_tokens=create_distinct_tokens(tokens)
    n=len(distinct_tokens)
    bi_gram_probabilities=probability_table(distinct_tokens,dct,dct1)
    bi_gram_prob={}

    # convert the list to the dictionary with bigrams as key 
    for i in range(n):
         for j in range(n):
             bi_gram_prob.update({(distinct_tokens[i],distinct_tokens[j]):bi_gram_probabilities[i][j]})

    return bi_gram_prob


    