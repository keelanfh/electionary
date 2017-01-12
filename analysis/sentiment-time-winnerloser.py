from __future__ import division

import json
import os
import urllib
from string import digits
from string import punctuation

import nltk

from commonfunctions import commonfunctions as cf

wnl = nltk.WordNetLemmatizer()

root_directory = os.path.dirname(os.path.abspath(os.curdir))
directory = os.path.join(root_directory, cf.working_directory)

# I have moved the graph code to a separate file so that the analysis does not have to be re-run every time
# you change something on the graph. This code can be run through Pypy to make it faster, but all sentiment
# analysis code is quite slow because of the quantity of data being handled.

# TODO Could be improved, again, removing the interventions of the moderators

# Analysis of the polarity of the transcripts
# Compares the transcripts with lists of positive and negative words
# Counts the matches and displays them in a graph
# Takes ages to run, but maybe that is just in my computer

# List all the files in the directory
filesList = os.listdir(directory)
# Create a list for all the objects imported to JSON to be added to
transcripts = []

# import positive and negative lists
# create empty lists for both

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

# Go through each file, open it, and add its content to the list
for myFile in filesList:
    with open(os.path.join(directory, myFile), 'r') as f:
        # Here, the JSON is converted back to a Python object
        transcript = json.load(f)
    transcripts.append(transcript)

all_list = []

# Loop through the three 'parties': 'r' - republican; 'd' - democrat; 't' - anything else
for winnerloser in ['w', 'l']:

    transcript_results = []
    # Go through each transcript
    for transcript in transcripts:

        # Get the date - converting the ISO date back into a datetime.date object
        year = cf.iso_to_datetime(transcript['date']).year

        # Create a string for all of the text in the debate
        allText = ""

        # Add all the text spoken by speakers to that string
        for speaker in transcript['text_by_speakers']:
            if 'winnerloser' in speaker:
                if speaker['winnerloser'] == winnerloser or (speaker['winnerloser'] == 'n'
                                                             and winnerloser == 'l'):
                    print winnerloser
                    print cf.unicode_to_ascii(transcript['description'])
                    allText += (" " + speaker['text'])

        # removes punctuation, digits, splits text into words
        # remove words shorter than 3 characters and suffixes

        for p in list(punctuation):
            allText = allText.replace(p, '')

        for k in list(digits):
            allText = allText.replace(k, '')

        # Split, check for length, lemmatize
        long_words = [w for w in allText.split() if len(w) > 3]
        long_words = [wnl.lemmatize(w) for w in long_words]

        word_count = len(long_words)

        total_pos_words = len([True for x in long_words if x in positive_words])
        total_neg_words = len([True for x in long_words if x in negative_words])
        print total_pos_words, total_neg_words, word_count, year
        transcript_results.append(dict(total_pos_words=total_pos_words, total_neg_words=total_neg_words,
                                       word_count=word_count, year=year))

    # Get a unique list of the years
    uniqueYears = list(set([cf.campaign_year_from_year(transcript_result['year'])
                            for transcript_result in transcript_results]))
    uniqueYears.sort()
    print uniqueYears
    year_results = []

    # For each unique year
    for uniqueYear in uniqueYears:

        transcript_results_for_year = [transcript_result for transcript_result in transcript_results
                                       if cf.campaign_year_from_year(transcript_result['year']) == uniqueYear]

        word_count = sum([transcript_result['word_count'] for transcript_result in transcript_results_for_year])

        if word_count:
            total_neg_words = sum(
                [transcript_result['total_neg_words'] for transcript_result in transcript_results_for_year])

            total_pos_words = sum(
                [transcript_result['total_pos_words'] for transcript_result in transcript_results_for_year])

            year_results.append(
                dict(positive=total_pos_words / word_count, negative=total_neg_words / word_count,
                     word_count=word_count, year=uniqueYear))

    all_list.append(dict(winnerloser=winnerloser, year_results=year_results))

with open('sentiment-time-winnerloser.json', 'w') as f:
    json.dump(all_list, f)
