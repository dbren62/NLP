from textblob import TextBlob
import nltk

#nltk.download("stopwords")
from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd

blob = TextBlob(Path("book of John text.txt").read_text())

stops = stopwords.words("english")

more_stops = ["thy", "ye", "verily", "thee", "hath", "say", "thou", "art", "shall"]
stops += more_stops
#print(stops)

# call the blob.word_counts dictionary's item method to get a list of the word frequency
items = blob.word_counts.items()
#print(items)

nouns = blob.noun_phrases

cleaned_list = [word for word in items if word[0] not in stops]
#print(cleaned_list)

noun_list = [word for word in cleaned_list if word[0] in nouns]
#print(noun_list)

from operator import itemgetter

sorted_items = sorted(cleaned_list, key=itemgetter(1), reverse=True)
top15 = sorted_items[:15]

sorted_nouns = sorted(noun_list, key=itemgetter(1), reverse=True)
top15nouns = sorted_nouns[:15]
print(top15nouns)

from wordcloud import WordCloud
import imageio

#top15list = [word[0] for word in top15nouns]
#text = " ".join(top15list)
#print(text)

#mask_image = imageio.imread("mask_circle.png")

wordcloud = WordCloud(colormap="turbo", background_color="white")

wordcloud = wordcloud.generate_from_frequencies(dict(top15nouns))
#wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("BookOfJohnCircle.png")

plt.imshow(wordcloud)
print("done")