from __future__ import division
import json
import datetime as dt
from string import punctuation
from string import digits
import nltk
import urllib

wnl = nltk.WordNetLemmatizer()

files = ['negative.txt', 'positive.txt']

path = 'http://www.unc.edu/~ncaren/haphazard/'
for file_name in files:
    urllib.urlretrieve(path + file_name, file_name)

positive_words = open("positive.txt").read()
positive_words = positive_words.split('\n')
positive_counts = []

negative_words = open('negative.txt').read()
negative_words = negative_words.split('\n')
negative_counts = []


def text_to_datetime(date_string):
    month = date_string[4:7]
    day = date_string[8:10]
    hour = date_string[11:13]
    minute = date_string[14:16]
    second = date_string[17:19]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
              "Nov", "Dec"]
    month = int(months.index(month) + 1)
    return dt.datetime(year=2016, month=month, day=int(day), hour=int(hour), minute=int(minute), second=int(second))


with open('HillaryClintonTweets.json', 'r') as f:
    statuses = json.load(f)

results = []
y = len(statuses)

for index, status in enumerate(statuses):
    text = status['text']
    for p in list(punctuation):
        text = text.replace(p, '')

    for k in list(digits):
        text = text.replace(k, '')

    # Split, check for length, lemmatize
    long_words = [w for w in text.split() if len(w) > 3]
    long_words = [wnl.lemmatize(w) for w in long_words]

    word_count = len(long_words)

    total_pos_words = len([True for x in long_words if x in positive_words])
    total_neg_words = len([True for x in long_words if x in negative_words])
    date = text_to_datetime(status['created_at'])
    total_pos_words /= word_count
    total_neg_words /= word_count

    results.append(dict(total_pos_words=total_pos_words, total_neg_words=total_neg_words,
                        word_count=word_count, date=date.isoformat()))

    print "Progress: " + str((index / y) * 100) + "%"

with open('HillaryClintonTweetsResults.json', 'w') as f:
    json.dump(results, f)
