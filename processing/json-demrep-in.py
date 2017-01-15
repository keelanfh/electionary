import csv
import json
import os
import unicodedata

import commonfunctions as cf

csvfile = 'json-demrep.csv'

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
    print csvoutput2[transcriptno][0][0], '\n', unicodedata.normalize('NFKD', transcript['description']).encode(
        'ascii', 'ignore')
    assert csvoutput2[transcriptno][0][0] == unicodedata.normalize('NFKD', transcript['description']).encode(
        'ascii', 'ignore')
    # print csvoutput2
    # print [x for x in csvoutput2[transcriptno] if x[0] == 't' or x[0] == 'r' or x[0] == 'd']
    for speaker in [x for x in csvoutput2[transcriptno] if x[0] == 't' or x[0] == 'r' or x[0] == 'd']:
        for speakerdict in transcript['text_by_speakers']:
            if unicodedata.normalize('NFKD', speakerdict['speaker']).encode(
                    'ascii', 'ignore') == speaker[2]:
                speakerdict['party'] = speaker[0]
#
# for transcript in transcripts:
#     print transcript

# for transcript in transcripts:
#     print [[x['speaker'], x['party']] for x in transcript['text_by_speakers'] if 'party' in x]

if 'transcripts-3rdJan' not in os.listdir(os.curdir):
    os.mkdir('transcripts-3rdJan')

for fileno, file in enumerate(filesList):
    with open(os.path.join('transcripts-3rdJan', file), 'w') as f:
        json.dump(transcripts[fileno], f)


        # index = 0
        #
        # for rowno, row in enumerate(csvreader):
        #     # If it's a division...
        #     if row[0][0:3] == "XXX":
        #         # Check that the description matches
        #         assert csvreader[rowno + 1][0] == \
        #                unicodedata.normalize('NFKD', transcripts[index]['description']).encode('ascii', 'ignore')
        #         if csvreader[rowno + 2][0] == 't' or csvreader[rowno + 2][0] == 'r' or csvreader[rowno + 2][0] == 'd':
        #             for row2 in csvreader[rowno:]:
        #                 if row2[0][0:3] == "XXX":
        #                     index += 1
        #                     break
        #                 for speaker in transcripts[index]['text_by_speakers']:
        #                     if speaker['speaker'] == csvreader[rowno + 2][1]:
        #                         speaker['party'] = csvreader[rowno + 2][0]
        #         elif csvreader[rowno + 3][0] == 't' or csvreader[rowno + 3][0] == 'r' or csvreader[rowno + 3][0] == 'd':
        #             for row2 in csvreader[rowno:]:
        #                 if row2[0][0:3] == "XXX":
        #                     index +=1
        #                     break
        #                 for speaker in transcripts[index]['text_by_speakers']:
        #                     if speaker['speaker'] == csvreader[rowno + 2][1]:
        #                         speaker['party'] = csvreader[rowno + 2][0]
        #
        # for file in filesList:
        #     with open(os.join('transcripts-2ndJan',filesList[f]), 'w') as f:
        #         json.dump(transcripts,f)
