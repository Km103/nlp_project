def calculate_accuracy(original_text, filled_text):
    original_words = original_text.split()
    filled_words = filled_text.split()
    correct_count = sum(1 for original, filled in zip(original_words, filled_words) if original == filled)
    total_words = len(original_words)
    accuracy = (correct_count / total_words) * 100
    return accuracy