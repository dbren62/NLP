from textblob import TextBlob
import nltk

# nltk.download("stopwords")
from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())
"""
print(blob.word_counts["juliet"])

print(blob.word_counts["romeo"])

print(blob.word_counts["thou"])

print(blob.words.count("joy"))

print(blob.noun_phrases.count("lady capulet"))

stops = stopwords.words("english")

more_stops = ["thee", "thy", "thou", "'"]
stops += more_stops

# print(stops)

# Let's call the blob.word_counts dictionary's item method to get a list of the word frequency
items = blob.word_counts.items()
print(items)

cleaned_list = [word for word in items if word[0] not in stops]
print(cleaned_list)
# the expression word[0] gets teh word from each tuple so we can check whether its in stop_words


# To determine the top 20 most frequent words, sort the tuples in descending order by word count.

from operator import itemgetter

#sorted_items = sorted(items)

sorted_items = sorted(cleaned_list, key=itemgetter(1), reverse=True)
print(sorted_items[:10])

top20 = sorted_items[:20]

print(top20)

df = pd.DataFrame(top20, columns=["word", "count"])

print(df)

import matplotlib.pyplot as plt

df.plot.bar(
    x="word", y="count", rot=0, legend=False, color=["y", "c", "m", "b", "g", "r"]
)

plt.gcf().tight_layout()

plt.show()
"""
#WORDCLOUD - Make sure to install wordcloud

from pathlib import Path
from wordcloud import WordCloud
import imageio

text = Path("RomeoAndJuliet.txt").read_text()
#print(text)

mask_image = imageio.imread("mask_heart.png")

wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")

plt.imshow(wordcloud)
print("done")

