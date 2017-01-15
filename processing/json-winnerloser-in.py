import csv
import json
import os
import unicodedata

import commonfunctions as cf

csvfile = 'json-winnerloser.csv'

root_directory = os.path.abspath(os.path.dirname(os.path.abspath(os.curdir)))
directory = os.path.join(root_directory, cf.working_directory)

# Produce CSV for us to sort out democratic and republican nominees

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

allSpeakers = []
with open(csvfile, 'r') as f:
    csvreader = csv.reader(f, delimiter=';')
    csvreader = [row for row in csvreader]

csvoutput = []
for rowno, row in enumerate(csvreader):
    if row[0][0:3] == "XXX":
        csvoutput.append(csvreader[rowno + 1:])

csvoutput2 = []
for output in csvoutput:
    for rowno, row in enumerate(output):
        if row[0][0:3] == "XXX":
            csvoutput2.append(output[:rowno])
            break

for transcriptno, transcript in enumerate(transcripts):
    print csvoutput2[transcriptno][0][0], '\n', unicodedata.normalize(
        'NFKD', transcript['description']).encode('ascii', 'ignore').replace(';', '').replace(',', '')
    assert csvoutput2[transcriptno][0][0].replace(';', '').replace(',', '') == unicodedata.normalize(
        'NFKD', transcript['description']).encode(
        'ascii', 'ignore').replace(';', '').replace(',', '')
    print csvoutput2
    print [x for x in csvoutput2[transcriptno] if x[0] == 'w' or x[0] == 'l' or x[0] == 'n']
    for speaker in [x for x in csvoutput2[transcriptno] if x[0] == 'w' or x[0] == 'l' or x[0] == 'n']:
        for speakerdict in transcript['text_by_speakers']:
            if unicodedata.normalize('NFKD', speakerdict['speaker']).encode(
                    'ascii', 'ignore') == speaker[2]:
                speakerdict['winnerloser'] = speaker[0]

for transcript in transcripts:
    print [[x['speaker'], x['winnerloser']] for x in transcript['text_by_speakers'] if 'winnerloser' in x]

if 'transcripts' not in os.listdir(root_directory):
    os.mkdir(os.path.join(root_directory, 'transcripts'))

for fileno, file in enumerate(filesList):
    with open(os.path.join(root_directory, 'transcripts', file), 'w') as f:
        json.dump(transcripts[fileno], f)
