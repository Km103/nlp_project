
from preprocess import preprocess_text
from stopwords import stop_words
from frequency import freq
from word_cloud import cloud
from tokenise import createToken
from pos_tagging import tagging
# Open a text file in read mode
with open('Orwell-1949 1984.txt', 'r') as file:
    book = file.read()

modified_book=preprocess_text(book)

filtered_book=stop_words(modified_book)

freqTable=freq(filtered_book)

#printing the tokens freq distribution 
for token, frequency in freqTable:
    print(f'{token}: {frequency}')


#cloud(createToken(filtered_book))

tagging(createToken(filtered_book))





