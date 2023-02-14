#import the spacy library
import spacy

#load the spacy library and store to a variable
nlp = spacy.load('en_core_web_md')

#store words as nlp
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

#adding my own word
word4 = nlp("teeth")

#print the word similarity
#cat - monkey
print(word1.similarity(word2))
#banana - monkey
print(word3.similarity(word2))

#banana - cat
print(word3.similarity(word1))

print("\n", word4.text)
#teeth - cat
print(word4.similarity(word1))

#teeth - monkey
print(word4.similarity(word2))

#teeth - banana
print(word4.similarity(word3))

"""
It is interesting to note here that teeth has less of a
similarity to the other words. Monkey and Cat are more similar
than monkey - teeth and cat - teeth, even though both animals have
teeth. Cat, however has a stronger similarity, probably due to 
cats being known to bite people and things. Banana has less 
similarity than the rest, even though you eat fruit with teeth.
"""

#create a variable with nlp words
tokens = nlp("cat apple monkey banana")

#create a for loop to compare each word to each other
for token1 in tokens:
    print("\n"  + token1.text)
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#styling
print("")

#create a sentence to compare
sentence_to_compare = "Why is my cat on the car"

#create a list of sentences to compare
sentences = ["Where did my dog go", 
"Hello, there is my car", 
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

#convert the sentence to compare into nlp
model_sentence = nlp(sentence_to_compare)

#for each sentence, check the similarity
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


#Do it all again, except with en_core_web_sm
print("\nThis is with en_core_web_sm now\n")
#load the spacy library and store to a variable
nlp = spacy.load('en_core_web_sm')

#store words as nlp
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

#adding my own word
word4 = nlp("teeth")

#print the word similarity
#cat - monkey
print(word1.similarity(word2))
#banana - monkey
print(word3.similarity(word2))

#banana - cat
print(word3.similarity(word1))

print("\n", word4.text)
#teeth - cat
print(word4.similarity(word1))

#teeth - monkey
print(word4.similarity(word2))

#teeth - banana
print(word4.similarity(word3))

#create a variable with nlp words
tokens = nlp("cat apple monkey banana")

#create a for loop to compare each word to each other
for token1 in tokens:
    print("\n"  + token1.text)
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#styling
print("")

#create a sentence to compare
sentence_to_compare = "Why is my cat on the car"

#create a list of sentences to compare
sentences = ["Where did my dog go", 
"Hello, there is my car", 
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

#convert the sentence to compare into nlp
model_sentence = nlp(sentence_to_compare)

#for each sentence, check the similarity
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

"""
This is interesting because when I run the code, I get an warning
message stating that the model I am using has no word vectors included,
so it will base its similarities based on the taggers. This means that 
the data could be incorrect. For example, banana - apple now has
an incredibly low similarity even though they are both fruits.
"""