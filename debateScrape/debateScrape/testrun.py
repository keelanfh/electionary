from __future__ import division
import cProfile as cp
from string import punctuation
from string import digits
import urllib
import commonfunctions as cf
import json
import os
import numpy as np
import matplotlib.pyplot as plt
import nltk

def main_thing(transcripts):
    years = []
    negative_words = []
    negative_counts = []
    positive_words = []
    positive_counts = []

    # Go through each transcript
    for transcript in transcripts:

        # Get the date - converting the ISO date back into a datetime.date object
        date = cf.iso_to_datetime(transcript['date'])
        year = date.year
        years.append(year)

        # Create a string for all of the text in the debate
        allText = ""

        # Add all the text spoken by speakers to that string
        for speaker in transcript['text_by_speakers']:
            if speaker == 'MODERATORS':
                break

            allText += (" " + speaker['text'])

            # removes punctuation, digits, splits text into words
            # remove words shorter than 3 characters and suffixes

            for p in list(punctuation):
                allText = allText.replace(p, '')

            for k in list(digits):
                allText = allText.replace(k, '')

            words = allText.split()

            long_words = [w for w in words if len(w) > 3]

            text = [wnl.lemmatize(t) for t in long_words]

        word_count = len(text)
        lengths.append(word_count)

        # count positive and negative words
        positive_counter = 0
        negative_counter = 0

        for word in text:
            if word in positive_words:
                positive_counter += 1
            elif word in negative_words:
                negative_counter += 1
        total_pos_words = positive_counter
        total_neg_words = negative_counter

        positive_counts.append(total_pos_words)
        negative_counts.append(total_neg_words)

        print year

    # Get a unique list of the years
    uniqueYears = list(set(years))

    # Create a new list for the sentiments corresponding to each year.
    uniquepositivewords = []
    uniquenegativewords = []

    # For each unique year
    for uniqueYear in uniqueYears:
        print uniqueYear
        # Create a list which will contain all sentiment values for a year
        positivewordsforyear = []
        negativewordsforyear = []

        # Go through all the different years, adding the sentiment to that list.
        for number, year in enumerate(years):
            if year == uniqueYear:
                positivewordsforyear.append(positive_counts[number] / lengths[number])

        for number, year in enumerate(years):
            if year == uniqueYear:
                negativewordsforyear.append(negative_counts[number] / lengths[number])

        # Take a simple mean of the sentiments of all texts in a given year.
        # Add this to the list uniqueSentiments, which is paired with the uniqueYears list.

        uniquepositivewords.append(np.mean(positivewordsforyear))

        uniquenegativewords.append(np.mean(negativewordsforyear))

# This creates two graphs, but only one is shown with the data for both positive and negative words.
# I don't know why this happens...
# Red is positive and blue is negative

# plt.plot(uniqueYears, uniquepositivewords, 'ro')
# plt.xlabel('Year')
# plt.ylabel('Positive Words')
# plt.show()
#
# plt.plot(uniqueYears, uniquenegativewords, 'bo')
# plt.xlabel('Year')
# plt.ylabel('Negative Words')
# plt.show()

cp.run('main_thing("foo|bar")')