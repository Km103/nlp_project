import matplotlib.pyplot as plt
import nltk
from nltk.probability import FreqDist

def createPlot(tokens):

    fdist = FreqDist(tokens)
    # Extract the most common tokens and their frequencies
    most_common_tokens = fdist.most_common(10)  # Adjust the number of tokens as needed

    # Extract token and frequency pairs
    tokens, frequencies = zip(*most_common_tokens)

    # Create a bar chart (histogram) of token frequencies
    plt.figure(figsize=(10, 6))
    plt.bar(tokens, frequencies)
    plt.xlabel('Tokens')
    plt.ylabel('Frequency')
    plt.title('Token Frequency Distribution')
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.tight_layout()

    # Show the histogram
    plt.show()