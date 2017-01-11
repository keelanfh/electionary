from __future__ import division
import urllib
from string import punctuation
from string import digits
import numpy as np
import os

class color:
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def processThis(someFile):
    with open(someFile, 'r') as f:
        articles = f.read()
    # remove capital letters, numbers and punctuation
    # split the text into words
    articles = articles.lower()
    for p in list(punctuation):
        articles = articles.replace(p, '')
    for k in list(digits):
        articles = articles.replace(k, '')

    articles_words = articles.split()
    print color.UNDERLINE + 'EXAMPLE' + color.END
    print '  '
    # total number of words
    word_count = len(articles_words)
    print color.UNDERLINE + 'Total number of words' + color.END
    print word_count
    print '  '
    # import positive and negative lists
    # create counters for both
    files = ['negative.txt', 'positive.txt']
    path = 'http://www.unc.edu/~ncaren/haphazard/'
    for file_name in files:
        urllib.urlretrieve(path + file_name, file_name)

    pos_words = open("positive.txt").read()
    positive_words = pos_words.split('\n')
    positive_counts = []
    neg_words = open('negative.txt').read()
    negative_words = neg_words.split('\n')
    negative_counts = []
    for k in articles_words:
        positive_counter = 0
        negative_counter = 0
    print '  '
    # count positive and negative words
    print color.UNDERLINE + 'Positive words in the text' + color.END
    for word in articles_words:
        if word in positive_words:
            positive_counter = positive_counter + 1
            print word

    print '  '
    print color.UNDERLINE + 'Negative words in the text' + color.END
    for word in articles_words:
        if word in negative_words:
            negative_counter = negative_counter + 1
            print word

    print '  '
    print color.UNDERLINE + 'Total number of positive words' + color.END
    print positive_counter
    print color.UNDERLINE + 'Total number of negative words' + color.END
    print negative_counter
    print '  '
    # relative positive and negative words
    print color.UNDERLINE + 'Relative positive words' + color.END
    pos = positive_counter / word_count
    print color.UNDERLINE + 'Relative negative words' + color.END
    neg = negative_counter / word_count
    # 155 most frequent words
    print '  '
    print color.UNDERLINE + '155 most frequent words:' + color.END
    word_counter = {}
    for word in articles_words:
        if len(word) > 0 and word != '\r\n':
            if word not in word_counter:  # if 'word' not in word_counter, add it, and set value to 1
                word_counter[word] = 1
            else:
                word_counter[word] += 1  # if 'word' already in word_counter, increment it by 1
    for i, word in enumerate(sorted(word_counter, key=word_counter.get, reverse=True)[:155
                             ]):
        # sorts the dict by the values, from top to botton, takes the 155 top items,
        print "%s: %s - %s" % (i + 1, word, word_counter[word])

    return [pos, neg]


# read text
filesList = os.listdir("debateScrape/debateScrape/transcripts-new")

clintonList, trumpList = [],[]

for file in filesList:
    if "CLINTON" in file and ".txt" in file:
        clintonList.append("debateScrape/debateScrape/transcripts-new/" + file)
    if "TRUMP" in file and ".txt" in file:
        trumpList.append("debateScrape/debateScrape/transcripts-new/" + file)

clintonPos, clintonNeg, trumpPos, trumpNeg = [], [], [], []

for file in clintonList:
    print file
    [pos,neg] = processThis(file)
    clintonPos.append(pos)
    clintonNeg.append(neg)

for file in trumpList:
    [pos,neg] = processThis(file)
    trumpPos.append(pos)
    trumpNeg.append(neg)

clintonPos = np.average(clintonPos)
clintonNeg = np.average(clintonNeg)
trumpPos = np.average(trumpPos)
trumpNeg = np.average(trumpNeg)

print ["clintonPos", clintonPos, "trumpPos", trumpPos]
print ["clintonNeg", clintonNeg, "trumpNeg", trumpNeg]