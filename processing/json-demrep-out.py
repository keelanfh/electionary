import csv
import json
import os
import unicodedata

import commonfunctions as cf

csvfile = 'json-demrep.csv'

root_directory = os.path.abspath(os.path.dirname(os.path.abspath(os.curdir)))
directory = os.path.join(root_directory, cf.working_directory)

# Produce a list of speakers
# So that we can find duplicate speaker names

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
with open(csvfile, 'w') as f:
    csvwriter = csv.writer(f, delimiter=';')
    # Go through each transcript
    for transcript in transcripts:

        speakers = [x['speaker'] for x in transcript['text_by_speakers']]
        csvwriter.writerow(['XXXXXXXXXXX'])
        for x in ['candidates', 'description', 'participants']:
            if x in transcript:
                transcript[x] = unicodedata.normalize('NFKD', transcript[x]).encode('ascii', 'ignore')
                csvwriter.writerow([transcript[x]])
        for speaker in speakers:
            speaker = unicodedata.normalize('NFKD', speaker).encode('ascii', 'ignore')
            if transcript['description'][0:len('Democrat')] == 'Democrat':
                csvwriter.writerow(['d', 'speaker', speaker])
            elif transcript['description'][0:len('Republican')] == 'Republican':
                csvwriter.writerow(['r', 'speaker', speaker])
            else:
                csvwriter.writerow(['', 'speaker', speaker])

