import random

# list that stores index of blanks
blank_positions=[]


def createBlank(tokens):
    # Choose a random position in the chapter to insert a blank
    blank_position = random.randint(1, len(tokens) - 2)

    # Check if the chosen position already has a blank
    while blank_position in blank_positions:
        blank_position = random.randint(1, len(tokens) - 2)
    
    # Record the position of the blank
    blank_positions.append(blank_position)

    #putting the blank in the text
    tokens[blank_position]="_"
    return tokens


def shannon(num_blanks,tokens,bi_gram_probabilities):

    # create multiple blanks
    for i in range(num_blanks):
        tokens=createBlank(tokens)
    
    for i in range(num_blanks):
        # previous word to the blank
        preceding_word = tokens[blank_positions[i]-1]

        # Predict the missing word based on the preceding word using bi-gram probabilities
        candidate_words = [(word2,prob) for (word1, word2), prob in bi_gram_probabilities.items() if word1 == preceding_word]


        # choosing word from list of possible words with maximum probability
        if candidate_words:
            m=len(candidate_words)
            prob=0.0
            for (w,p) in candidate_words:
                if(p>prob):
                    prob=p
                    missing_word=w
        else:
            # if preceding word is not found in the corpus taken 
            missing_word = "_____"

        # Insert the missing word into the chapter text
        tokens[i + 1] = missing_word

    # Join the tokens to form the complete text
    filled_text = ' '.join(tokens)

    return filled_text


