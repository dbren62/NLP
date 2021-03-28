from textblob import TextBlob

"""
text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

# print(blob)

# print(blob.sentences)

# print(blob.words)

# print(blob.tags)

# print(blob.noun_phrases)

# print(blob.sentiment)

# print(round(blob.sentiment.polarity, 3))

# print(round(blob.sentiment.subjectivity, 3))

sentences = blob.sentences

for sentence in sentences:
    print(sentence)
    print(sentence.sentiment)
    print(round(sentence.sentiment.polarity, 3))

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)

blob.detect_language()  # detect the language of the text
# return would be 'en'

spanish = blob.translate(to="es")
# translate to spanish

print(spanish)

from textblob import Word

index = Word("index")

print(index.pluralize())

cacti = Word("cacti")

print(cacti.singularize())

animals = TextBlob("dog cat fish bird").words

print(animals.pluralize())

word = Word("theyr")

print(word.spellcheck())

corrected_word = word.correct()

sentence = TextBlob("Ths sentense has missplled wrds.")

corrected_sentence = sentence.correct()

print(corrected_word)
print(corrected_sentence)

german = blob.translate(to="de")
print(german)


from textblob import Word

# stemming algorithms work by cutting off the end or the beginning of the word, taking into account a list of
# common prefixes and suffixes that can be found in an inflected word.

# varieties - would be varieti
# studies - would be studi

# Lemmatization, on the other hand, takes into consideration the morphological analysis of the words

word1 = Word("studies")
word2 = Word("varieties")

print(word1.lemmatize())
print(word2.lemmatize())

happy = Word("happy")

print(happy.definitions)


for synset in happy.synsets:
    print(synset)
    for lemma in synset.lemmas():
        print(lemma)
        print(lemma.name())

#antonyms
lemmas = happy.synsets[0].lemmas()
print(lemmas)

for lemma in lemmas[0].antonyms():
    print(lemma.name())
"""

import nltk

# nltk.download("stopwords")

from nltk.corpus import stopwords

stops = stopwords.words("english")

print(stops)

text = "Today is a beautiful day."

blob = TextBlob(text)

cleaned_list = [word for word in blob.words if word not in stops]
print(cleaned_list)
