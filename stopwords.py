import nltk
from nltk.corpus import stopwords
#nltk.download('stopwords')
#nltk.download('punkt')

def stop_words(text):
    words = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    # Join the filtered words back into a sentence
    content = ' '.join(filtered_words)
    return content