import random


def shannon(num_blanks,tokens,bi_gram_probabilities):
    # Define the number of blanks you want to insert

    blank_positions = []

    # Generate and fill blanks
    for _ in range(num_blanks):
        # Choose a random position in the chapter to insert a blank
        blank_position = random.randint(0, len(tokens) - 2)

        # Check if the chosen position already has a blank
        while blank_position in blank_positions:
            blank_position = random.randint(0, len(tokens) - 2)

        # Record the position of the blank
        blank_positions.append(blank_position)

        # Extract the preceding word
        preceding_word = tokens[blank_position]

        # Predict the missing word based on the preceding word using bi-gram probabilities
        candidate_words = [word2 for (word1, word2) in bi_gram_probabilities if word1 == preceding_word]

        # Randomly select a candidate word
        if candidate_words:
            missing_word = random.choice(candidate_words)
        else:
            missing_word = "_____"

        # Insert the missing word into the chapter text
        tokens[blank_position + 1] = missing_word


    # Join the tokens to form the complete text
    filled_text = ' '.join(tokens)

    return (filled_text,blank_positions)


