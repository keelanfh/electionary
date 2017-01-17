import json
import os
from commonfunctions import commonfunctions as cf

filenames = ['HillaryClintonTweets.json', 'realDonaldTrumpTweets.json']

for x in filenames:
    with open(os.path.abspath(os.path.join('twitter',x)), 'r') as f:
        tweets = json.load(f)

    tweets_text = [cf.unicode_to_ascii(tweet['text'].replace(u'\u2014', ' ')) for tweet in tweets]

    tweets_text = " ".join(tweets_text)

    with open(os.path.abspath(os.path.join('twitter', x[:-5] + '.txt')), 'w') as f:
        f.write(tweets_text)
