from preprocess import preprocess_text
from stopwords import stop_words
from frequency import freq
from word_cloud import cloud
from tokenise import createToken
from pos_tagging import tagging
from probabilities import getBiGramProb
from blanks import shannon,blank_positions
from accuracy import  calculate_accuracy
from plot import createPlot


# Open  book in read mode
with open('Orwell-1949 1984.txt', 'r') as file:
    book = file.read()

# Open  longest chapter in read mode
with open('chapter.txt', 'r') as file:
    chapter = file.read()

# Open other chapter  in read mode
with open('other_chapter.txt', 'r') as file:
    other_chapter = file.read()


# cleaning the text
modified_book=preprocess_text(book)

# filtering text by removing stopwords
filtered_book=stop_words(modified_book)

# creating/displaying  the frequncy table of various of various tokens
freqTable=freq(filtered_book)

#printing the tokens freq distribution 
for token, frequency in freqTable:
    print(f'{token}: {frequency}')


# creating the word cloud
cloud(createToken(filtered_book))

# creating the plot
createPlot(createToken(filtered_book))

# POS tagging using Penn Treebank 
tagging(createToken(filtered_book))

# cleaning the chapter
modified_chapter= preprocess_text(chapter)

# tokenising the chapter without removing stopwords
chapter_tokens=createToken(modified_chapter)

#creating and printing the bigram probabilities of the longest chapter 
bi_gram_prob=getBiGramProb(chapter_tokens)
#print(bi_gram_prob)

#cleaning the other chapter
modified_other_chapter= preprocess_text(other_chapter)

# creating tokens
other_chapter_tokens = createToken(modified_other_chapter)

original_text = ' '.join(other_chapter_tokens)

# create n blanks and predict the word using bi gram prob table created 
# earlier from the longest chapter. // Playing  Shannon game 
# lets have  n = 50

filled_text=shannon(50,other_chapter_tokens,bi_gram_prob)

# calculating accuracy

accuracy=calculate_accuracy(original_text,filled_text,blank_positions)
print("Accuracy: {:.2f}%".format(accuracy))









