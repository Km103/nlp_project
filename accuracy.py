def calculate_accuracy(original_text, filled_text,blank_positions):

    # number of correct counts 
    correct_count=0
    # number of blanks
    n=len(blank_positions)
    for i in range(n):
        pos=blank_positions[i]
        if(original_text[pos]==filled_text[pos]):
            correct_count=correct_count+1

    # accuracy that the blank has been filled with original value
    accuracy = (correct_count / n) * 100
    return accuracy