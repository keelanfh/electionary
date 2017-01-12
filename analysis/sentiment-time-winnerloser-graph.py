import csv
import json
import os

import matplotlib.pyplot as plt

from commonfunctions import commonfunctions as cf

root_directory = os.path.abspath(os.path.dirname(os.path.abspath(os.curdir)))
directory = os.path.join(root_directory, cf.working_directory)

with open('sentiment-time-winnerloser.json', 'r') as f:
    data = json.load(f)

w, l = None, None

for datum in data:
    if datum['winnerloser'] == 'w':
        w = datum['year_results']
    if datum['winnerloser'] == 'l':
        l = datum['year_results']

winnerPositiveData = [(x['year'], x['positive']) for x in w]
winnerNegativeData = [(x['year'], x['negative']) for x in w]

loserPositiveData = [(x['year'], x['positive']) for x in l]
loserNegativeData = [(x['year'], x['negative']) for x in l]

years = list(set([x['year'] for x in w]).union([x['year'] for x in l])).sort()

# # This bit writes to a file. Useful if you want a table of results
# with open('results.csv', 'w') as f:
#     dw = csv.DictWriter(f, r[0].keys())
#     csv.writer(f, ['Sentiment in Republican Debates'])
#     dw.writeheader()
#     dw.writerows(r)
#     csv.writer(f, ['Sentiment in Democrat Debates'])
#     dw.writeheader()
#     dw.writerows(d)

plt.style.use('ggplot')
fig = plt.figure(0)
ax = fig.gca()
ax.grid(b=False)
ax.set_axis_bgcolor('white')

labels = ['Winners', 'Losers']
colors = ['pink', 'purple']

for labelno, data in enumerate([winnerNegativeData, loserNegativeData]):
    data2 = zip(*data)
    ax.plot(data2[0], data2[1], label=labels[labelno], lw=2.5)

ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Proportion of words in  dictionaries')
ax.set_title('Negative Sentiment over time in US election debates, split by winners and losers', y=1.05)
plt.savefig(os.path.join(root_directory, 'images','analysis-sentiment-time-winnerloser-negative.svg'), format='svg')

fig = plt.figure(1)
ax = fig.gca()
ax.grid(b=False)
ax.set_axis_bgcolor('white')

for labelno, data in enumerate([winnerPositiveData, loserPositiveData]):
    data2 = zip(*data)
    ax.plot(data2[0], data2[1], label=labels[labelno], lw=2.5)

ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Proportion of words in  dictionaries')
ax.set_title('Positive Sentiment over time in US election debates, split by winners and losers', y=1.05)
plt.savefig(os.path.join(root_directory, 'images', 'analysis-sentiment-time-winnerloser-positive.svg'), format='svg')
