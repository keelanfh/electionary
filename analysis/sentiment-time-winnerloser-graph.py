import csv
import json
import os

import matplotlib.pyplot as plt

import commonfunctions as cf
import matplotlib as mpl

root_directory = os.path.abspath(os.path.dirname(os.path.abspath(os.curdir)))
directory = os.path.join(root_directory, cf.working_directory)

with open('sentiment-time-winnerloser.json', 'r') as f:
    data = json.load(f)

w = [datum['year_results'] for datum in data if datum['winnerloser'] == 'w'][0]
print w
l = [datum['year_results'] for datum in data if datum['winnerloser'] == 'l'][0]
print l

winnerPositiveData = [(x['year'], x['positive'], x['word_count']) for x in w]
winnerNegativeData = [(x['year'], x['negative'], x['word_count']) for x in w]

loserPositiveData = [(x['year'], x['positive'], x['word_count']) for x in l]
loserNegativeData = [(x['year'], x['negative'], x['word_count']) for x in l]

# def weighted_average(list_of_tuples):
#     assert type(list_of_tuples) == list
#     assert not [True for item in list_of_tuples if type(item) != tuple]
#     total = 0
#     total_weights = 0
#     for tuple_ in list_of_tuples:
#         amount, weight = tuple_
#         total += amount * weight
#         total_weights += weight
#     return total / total_weights
#
#
# years = list(set([x['year'] for x in w]).union([x['year'] for x in l]))
# years.sort()
#
# winnerPositiveData = []
# winnerNegativeData = []
# loserNegativeData = []
# loserPositiveData = []
#
# for year in years:
#     winnerPositiveData.append(
#         (year, weighted_average([(x[1], x[2]) for x in winnerPositiveData2 if x[0] == year])))
#     winnerNegativeData.append(
#         (year, weighted_average([(x[1], x[2]) for x in winnerNegativeData2 if x[0] == year])))
#     loserPositiveData.append(
#         (year, weighted_average([(x[1], x[2]) for x in loserPositiveData2 if x[0] == year])))
#     loserNegativeData.append(
#         (year, weighted_average([(x[1], x[2]) for x in loserNegativeData2 if x[0] == year])))
#
# print loserNegativeData

# # This bit writes to a file. Useful if you want a table of results
# with open('winnerloserDebug.csv', 'w') as f:
#     dw = csv.DictWriter(f, w[0].keys())
#     csv.writer(f, ['Sentiment in Republican Debates'])
#     dw.writeheader()
#     dw.writerows(w)
#     csv.writer(f, ['Sentiment in Democrat Debates'])
#     dw.writeheader()
#     dw.writerows(l)

plt.style.use('ggplot')
fig = plt.figure(0)
ax = fig.gca()
ax.grid(b=False)
ax.set_axis_bgcolor('white')

labels = ['Winners', 'Losers']
colors = ['#7fbf7b', '#af8dc3']

for labelno, data in enumerate([winnerNegativeData, loserNegativeData]):
    data2 = zip(*data)
    ax.plot(data2[0], data2[1], color=colors[labelno], label=labels[labelno], lw=2.5)

ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Proportion of words in dictionary of negative words')
ax.set_title('Negative Sentiment over time in US election debates, split by winners and losers',
             fontdict={'fontsize': 13,
                       'fontweight': mpl.rcParams['axes.titleweight'],
                       'verticalalignment': 'baseline',
                       'horizontalalignment': 'center'},
             y=1.05)
plt.savefig(os.path.join(root_directory, 'images', 'analysis-sentiment-time-winnerloser-negative.svg'), format='svg')

fig = plt.figure(1)
ax = fig.gca()
ax.grid(b=False)
ax.set_axis_bgcolor('white')

for labelno, data in enumerate([winnerPositiveData, loserPositiveData]):
    data2 = zip(*data)
    print data2
    ax.plot(data2[0], data2[1], color=colors[labelno], label=labels[labelno], lw=2.5)

ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Proportion of words in dictionary of positive words')
ax.set_title('Positive Sentiment over time in US election debates, split by winners and losers',
             fontdict={'fontsize': 13,
                       'fontweight': mpl.rcParams['axes.titleweight'],
                       'verticalalignment': 'baseline',
                       'horizontalalignment': 'center'},
             y=1.05)
plt.savefig(os.path.join(root_directory, 'images', 'analysis-sentiment-time-winnerloser-positive.svg'), format='svg')
