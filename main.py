import re
import json
from tkinter import W
import math


data_file = open("../archive/yelp_academic_dataset_business.json")
data = []

#read 10k first lines and print

for line in data_file:
    data.append(json.loads(line))['text']
    #text += obj.get("text")
    if len(data) == 10000:
        break

data_file.close()

print(len(data))

#chang non-word letter to text
text = re.sub(r"\W", "", text)

#get word from text
words = text.split()

uniqWords = ()
for word in words:
    if word in uniqWords:
        uniqWords[word] +=1
    else:
        print(f"new word {word}")
        uniqWords[word] = 1
    if len(uniqWords) > 100:
        break;
print(uniqWords)

#calculate idf
def idf(word,text):
    return math.log(1/df(word, text))

#calculate tf
def tf(word, occ):
    return occ[word]

def tfidf (word, text, occ):
    return tf(word, occ) * idf(word, text)

print(f"Document has a total of {len(text)} characters")
occ = countOccurrence(text)
print(occ)
