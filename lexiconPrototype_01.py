# This is a lexicon Based Sentiment Analysis Algorithm 
# LEXICON https://github.com/cjhutto/vaderSentiment/blob/master/vaderSentiment/vader_lexicon.txt


# Sentiment analyzer NLTK 
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk import tokenize

sentences = ["Great place to be when you are in Bangalore.",
"The place was being renovated when I visited so the seating was limited.",
"Loved the ambience, loved the food",
"The food is delicious but not over the top.",
"Service - Little slow, probably because too many people.",
"The place is not easy to locate",
"Mushroom fried rice was tasty"]

#tokenize.sent_tokenize(str(hotel_rev))

sid = SentimentIntensityAnalyzer()
for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]))
