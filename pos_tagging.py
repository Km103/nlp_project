import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

#download the treebank corpus from nltk
#nltk.download('treebank')

#download the universal tagset from nltk
#nltk.download('universal_tagset')

def tagging(tokens):
    #performs POS tagging using Penn Treebank
    tagged_words = nltk.pos_tag(tokens)

    # Create a frequency distribution of PoS tags
    tag_fd = nltk.FreqDist(tag for (word, tag) in tagged_words)

    tag_fd.tabulate()

    
