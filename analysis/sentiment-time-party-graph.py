import csv
import json
import os

import matplotlib.pyplot as plt

import commonfunctions as cf

root_directory = os.path.abspath(os.path.dirname(os.path.abspath(os.curdir)))
directory = os.path.join(root_directory, cf.working_directory)

with open('sentiment-time-party.json', 'r') as f:
    data = json.load(f)

r, d = None, None

for datum in data:
    if datum['party'] == 'r':
        r = datum['year_results']
    if datum['party'] == 'd':
        d = datum['year_results']

repPositiveData = [(x['year'], x['positive']) for x in r]
repNegativeData = [(x['year'], x['negative']) for x in r]

demPositiveData = [(x['year'], x['positive']) for x in d]
demNegativeData = [(x['year'], x['negative']) for x in d]

years = list(set([x['year'] for x in r]).union([x['year'] for x in d])).sort()

with open('results.csv', 'w') as f:
    dw = csv.DictWriter(f, r[0].keys())
    csv.writer(f, ['Sentiment in Republican Debates'])
    dw.writeheader()
    dw.writerows(r)
    csv.writer(f, ['Sentiment in Democrat Debates'])
    dw.writeheader()
    dw.writerows(d)

plt.style.use('ggplot')
fig = plt.figure(0)
ax = fig.gca()
ax.grid(b=False)
ax.set_axis_bgcolor('white')

labels = ['Republican', 'Democrat']
colors = ['red', 'blue']

for labelno, data in enumerate([repNegativeData, demNegativeData]):
    data2 = zip(*data)
    ax.plot(data2[0], data2[1], label=labels[labelno], lw=2.5)

ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Proportion of words in  dictionaries')
ax.set_title('Negative Sentiment over time in US democratic/republican election debates', y=1.05)
plt.savefig(os.path.join(root_directory, 'images','analysis-sentiment-time-party-negative.svg'), format='svg')

fig = plt.figure(1)
ax = fig.gca()
ax.grid(b=False)
ax.set_axis_bgcolor('white')

for labelno, data in enumerate([repPositiveData, demPositiveData]):
    data2 = zip(*data)
    ax.plot(data2[0], data2[1], label=labels[labelno], lw=2.5)

ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Proportion of words in  dictionaries')
ax.set_title('Positive Sentiment over time in US democratic/republican election debates', y=1.05)
plt.savefig(os.path.join(root_directory, 'images', 'analysis-sentiment-time-party-positive.svg'), format='svg')
