from __future__ import division

import json
import os
import urllib
from string import digits
from string import punctuation

import nltk

from commonfunctions import commonfunctions as cf

if not cf.is_pypy():
    raise Exception('Change interpreter to pypy')

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
common_words = open("commonwordsenglish.txt").read().split()

root_directory = os.path.dirname(os.path.abspath(os.curdir))
directory = os.path.join(root_directory, cf.working_directory)

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
noun_numbers = []

# Go through each transcript
for transcript in transcripts:

    # Get the date - converting the ISO date back into a datetime.date object
    date = cf.iso_to_datetime(transcript['date'])
    uniqueYear = date.year
    years.append(uniqueYear)
    print uniqueYear

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

    # Lemmatize the words, removes suffixes (plurals, verb terminations etc)

    text = [wnl.lemmatize(t) for t in words]

    # tag all words in the text according to what type of word they are (nouns, verbs etc)
    # create a string for nouns
    # filter the nouns and add them to the emptystring

    text_tagged = nltk.pos_tag(text)

    nouns = [word for word, pos in text_tagged
             if pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS']
    noun_numbers.append(len(nouns))

    simplewords = len([True for word in nouns if word in common_words])

    # count how many of the 1000 common nouns appear on transcripts
    # add it to the list "simplicity"

    simplicity.append(simplewords)

# Get a unique list of the years
uniqueYears = list(set(years))

# Create a new list for the simplicity corresponding to each year.
uniquesimplewords = []

# For each unique year
for uniqueYear in uniqueYears:
    # Create a list which will contain all simplicity values for a year
    simplewordsforyear = []
    nounsforyear = []

    # Go through all the different years, adding the simplicity to that list and dividing
    # it over the total number of nouns.

    for number in range(len(years)):
        if cf.campaign_year_from_year(years[number]) == uniqueYear:
            simplewordsforyear.append(simplicity[number])
            nounsforyear.append(noun_numbers[number])

    # Take a simple mean of the simplicity of all texts in a given year.
    # Add this to the list uniquesimplewords, which is paired with the uniqueYears list.
    if sum(nounsforyear):
        uniquesimplewords.append(sum(simplewordsforyear)/sum(nounsforyear))

with open('complexity-over-time.json', 'w') as f:
    json.dump([[year for year in uniqueYears if not year % 4], uniquesimplewords], f)

# # The graph plots on the Y axis the relative amount of common nouns
#
# plt.plot(uniqueYears, uniquesimplewords, 'ro')
# plt.xlabel('Year')
# plt.ylabel('Common Nouns')
# plt.show()
