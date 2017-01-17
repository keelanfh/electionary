# Simply output a text file with all of Trump's speeches in debates

import json
import os
from commonfunctions import commonfunctions as cf

dir = 'transcripts'

transcripts = []
for filename in os.listdir(dir):
    with open(os.path.join(dir, filename)) as f:
        transcripts.append(json.load(f))

trump_speeches = []
for transcript in transcripts:
    if cf.iso_to_datetime(transcript['date']).year > 2012:
        for speaker_text in transcript['text_by_speakers']:
            if 'trump' in speaker_text['speaker'].lower():
                speaker_text['text'] = speaker_text['text'].replace(u'\u2014', ' ')
                trump_speeches.append(cf.unicode_to_ascii(speaker_text['text']))

trump_speeches = " ".join(trump_speeches)

with open('trumpspeeches.txt', 'w') as f:
    f.write(trump_speeches)