from __future__ import division
from string import punctuation
from string import digits
import urllib
import commonfunctions as cf
import json
import os
import plotly.plotly as py
import nltk

wnl = nltk.WordNetLemmatizer()

directory = cf.working_directory

# Analysis of the polarity of the transcripts
# Compares the transcripts with lists of positive and negative words
# Counts the matches and displays them in a graph
# Takes ages to run, but maybe that is just in my computer
# Could be improved, again, removing the interventions of the moderators
# Also, the name of the Y axis has to be changed and a legend has to be added

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

pos_words = open("positive.txt").read()
positive_words = pos_words.split('\n')
positive_counts = []

neg_words = open('negative.txt').read()
negative_words = neg_words.split('\n')
negative_counts = []

# Go through each file, open it, and add its content to the list
for myFile in filesList:
    with open(os.path.join(directory, myFile), 'r') as f:
        # Here, the JSON is converted back to a Python object
        transcript = json.load(f)
    transcripts.append(transcript)

# Create lists for the years and the length of the text for each year.
years = []
lengths = []

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

    uniquepositivewords.append(cf.mean(positivewordsforyear))

    uniquenegativewords.append(cf.mean(negativewordsforyear))

py.plot([{
    'x': uniqueYears,
    'y': uniquepositivewords},{'x':uniqueYears, 'y': uniquenegativewords}])
