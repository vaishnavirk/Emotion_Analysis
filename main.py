# Cleaning Text steps
# 1) Create a text file and take a text from it
# 2) Convert the letter into lowercase ( Apple is not equal to apple
# 3) remove punctuations like .,!? etc. (Hi! This is beautiful.)


import string
from collections import Counter
import matplotlib.pyplot as plt

# take the text from .txt file
# most of the blog articles are of type utf-8 type
text = open('read.txt', encoding='utf-8').read()
#print(text)
# converting into lower case
lower_case = text.lower()
#print(lower_case)

# To see all the punctuations present in python
# print(string.punctuation)
# removing punctuations
# .translate removes all the punctuations from the string
# str1 : specifies the list of characters that need to be replaced
# str2 : specifies the list of characters with which the characters need to be replaced
# str3 : specifies the list of characters that needs to be deleted
# Returns : returns the translation table which specifies the conversion that can be used
# maketrans creates a table oe-one function for translation
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
#print(cleaned_text)

# Tokenization : In Python tokenization basically refers to splitting up a larger body of text into smaller lines, words

# It is split and stored as a list in token_words
token_words = cleaned_text.split()
#print(token_words)

# Stop words : top words are words that don't add any meaning to our sentence which are filtered out before or after processing of natural language data
# So that timing of analysis of sentence becomes less
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing the stop words
final_word = []
for word in token_words:
    if word not in stop_words:
        final_word.append(word)

#print(final_word)

# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotiontxt
#    - open the emotion file
#    - loop through each file and clear it
#    - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list

emotion_list = []
# r denotes only readable
with open('emotions.txt', 'r') as file:
    for line in file:
        # prints all the lines in the file
        # print(line)
        # to replace all the new line feed with nothing
        clear_line = line.replace('\n', '')
        # print(clear_line)
        clear_line = clear_line.replace(',', '').replace("'", '')
        # print(clear_line)
        # to remove space at the front by using .strip() function
        clear_line = clear_line.strip()
        #print(clear_line)
        # to seperate word and associated emotion using split() using :
        word, emotion = clear_line.split(':')
        #print("Word :" + word + " "+ "Emotion :" + emotion)

        # now we have all the words to check in text in word list
        # step 2
        if word in final_word:
            emotion_list.append(emotion)


#print(emotion_list)
w = Counter(emotion_list)
print(w)

fig, axl = plt.subplots()
axl.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()






