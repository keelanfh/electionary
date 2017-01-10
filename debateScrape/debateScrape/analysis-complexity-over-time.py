from __future__ import division

import urllib

import commonfunctions as cf
import json
import os
import nltk
from string import punctuation
from string import digits

wnl = nltk.WordNetLemmatizer()

# This code compares the debate transcripts with the 1000 most common nouns used in the (US) English language.
# Counts the matches and displays them by year on a graph.
# I am sure the code has many errors that can be improved
# (for example not taking into account the moderators' interventions)
# But the results seem to match with our initial thoughts (trend towards simpler language)

# open the file with the 1000 most common nouns in US English

if 'commonwordsenglish.txt' not in os.listdir(os.curdir):
    urllib.urlretrieve(
        'https://gist.githubusercontent.com/deekayen/4148741/raw/01c6252ccc5b5fb307c1bb899c95989a8a284616/1-1000.txt',
        'commonwordsenglish.txt')
common_words = open("commonwordsenglish.txt").read()

directory = cf.working_directory

# List all the files in the directory
filesList = os.listdir(directory)
# Create a list for all the objects imported to JSON to be added to
transcripts = []

# Go through each file, open it, and add its content to the list
for myFile in filesList:
    with open(os.path.join(directory, myFile), 'r') as f:
        # Here, the JSON is converted back to a Python object
        transcript = json.load(f)
    transcripts.append(transcript)

# Create lists for the years, the simplicity and the number of nouns for each year.
years = []
simplicity = []
nouns = []

# Go through each transcript
for transcript in transcripts:

    # Get the date - converting the ISO date back into a datetime.date object
    date = cf.iso_to_datetime(transcript['date'])
    year = date.year
    years.append(year)
    print year

    # Create a string for all of the text in the debate
    allText = ""

    # Add all the text spoken by speakers to that string
    for speaker in transcript['text_by_speakers']:
        allText += (" " + speaker['text'])

    # Remove digits, punctuation and split the string into words
    for p in list(punctuation):
        allText = allText.replace(p, '')

    for k in list(digits):
        allText = allText.replace(k, '')

    words = allText.split()

    # Remove short words (shorter than 3 characters) because they dont usually have much meaning
    # Lemmatize the words, removes suffixes (plurals, verb terminations etc)

    long_words = [w for w in words if len(w) > 3]

    text = [wnl.lemmatize(t) for t in long_words]

    # tag all words in the text according to what type of word they are (nouns, verbs etc)
    # create a string for nouns
    # filter the nouns and add them to the emptystring

    text_tagged = nltk.pos_tag(text)

    stringnouns = ""

    numberofnouns = len([True for word, pos in text_tagged
                         if pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'])
    nouns.append(numberofnouns)

    simplewords = len([True for word in text if word in common_words.split()])
    # count how many of the 1000 common nouns appear on transcripts
    # add it to the list "simplicity"

    relativesimplewords = simplewords / numberofnouns

    simplicity.append(relativesimplewords)

# Get a unique list of the years
uniqueYears = list(set(years))

# Create a new list for the simplicity corresponding to each year.
uniquesimplewords = []

# For each unique year
for year in uniqueYears:
    # Create a list which will contain all simplicity values for a year
    simplewordsforyear = []

    # Go through all the different years, adding the simplicity to that list and dividing 
    # it over the total number of nouns.

    for number in range(len(years)):
        if years[number] == year:
            simplewordsforyear.append(simplicity[number] / nouns[number])

    # Take a simple mean of the simplicity of all texts in a given year.
    # Add this to the list uniquesimplewords, which is paired with the uniqueYears list.

    uniquesimplewords.append(cf.mean(simplewordsforyear))

with open('analysis-complexity-over-time.json', 'w') as f:
    json.dump([uniqueYears,uniquesimplewords], f)

# # The graph plots on the Y axis the relative amount of common nouns
#
# plt.plot(uniqueYears, uniquesimplewords, 'ro')
# plt.xlabel('Year')
# plt.ylabel('Common Nouns')
# plt.show()

import __future__