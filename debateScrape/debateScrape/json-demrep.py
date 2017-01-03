import commonfunctions as cf
import json
import csv
import os
import unicodedata

directory = cf.working_directory
csvfile = 'json-demrep.csv'

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

for rowno, row in enumerate(csvreader):
    if row[0][0:3] == "XXX":
        assert csvreader[rowno + 1][0] == transcripts[rowno]['description']
        if csvreader[rowno + 2][0] == 't' or csvreader[rowno + 2][0] == 'r' or csvreader[rowno + 2][0] == 'd':
            for row2 in csvreader[rowno:len(csvreader) + 1]:
                if row[0][0:3] == "XXX":
                    break
                for speaker in transcripts[rowno]['text_by_speakers']:
                    if speaker['speaker'] == csvreader[rowno + 2][1]:
                        speaker['party'] = csvreader[rowno + 2][0]
        elif csvreader[rowno + 3] == 't' or csvreader[rowno + 3] == 'r' or csvreader[rowno + 3] == 'd':
            for row2 in csvreader[rowno:len(csvreader) + 1]:
                if row[0][0:3] == "XXX":
                    break
                for speaker in transcripts[rowno]['text_by_speakers']:
                    if speaker['speaker'] == csvreader[rowno + 2][1]:
                        speaker['party'] = csvreader[rowno + 2][0]

for file in filesList:
    with open(os.join('transcripts-2ndJan',filesList[f]), 'w') as f:
        json.dump(transcripts,f)