import json
import os

from commonfunctions import commonfunctions as cf

dir = cf.working_directory

transcripts = []

for x in os.listdir(dir):
    with open(os.path.join(dir, x)) as f:
        transcripts.append(json.load(f))

with open('worldcitiesout.json', 'r') as f:
    city_dicts = json.load(f)

city_dicts = [x for x in city_dicts if x['Country'] == 'us']

results = []
for transcript in transcripts:
    description = transcript['description']
    date = transcript['date']
    for text in transcript['text_by_speakers']:
        for city_dict in city_dicts:
            index = text['text'].lower().find(" " + city_dict['City'] + " ")
            if index > 0:
                if index < 90:
                    from_index = 0
                else:
                    from_index = index - 100
                if len(text['text']) < index + 90:
                    to_index = len(text['text'])
                else:
                    to_index = index + 100
                result = ({'speaker': text['speaker'],
                           'city': city_dict,
                           'debate': {'description': description, 'date': date,
                                      'context': text['text'][from_index:to_index]}})
                print result
                results.append(result)

with open('city-mentions.json', 'w') as f:
    json.dump(results, f)