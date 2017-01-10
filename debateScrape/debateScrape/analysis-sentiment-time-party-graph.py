import matplotlib.pyplot as plt
import json
import csv

with open('analysis-sentiment-time-party.json', 'r') as f:
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



# plt.figure(0)
# labels = ['Republican', 'Democrat']
# for labelno, data in enumerate([repNegativeData, demNegativeData]):
#     data2 = zip(*data)
#     plt.plot(data2[0], data2[1], label=labels[labelno])
#
# plt.legend()
# plt.xlabel('Year')
# plt.ylabel('Proportion of words in  dictionaries')
# plt.title('Negative Sentiment over time in US democratic/republican election debates')
# plt.savefig('analysis-sentiment-time-party.svg', format='svg')
#
# plt.figure(1)
# for labelno, data in enumerate([repPositiveData, demPositiveData]):
#     data2 = zip(*data)
#     plt.plot(data2[0], data2[1], label=labels[labelno])
#
# plt.legend()
# plt.xlabel('Year')
# plt.ylabel('Proportion of words in  dictionaries')
# plt.title('Positive Sentiment over time in US democratic/republican election debates')
# plt.savefig('analysis-sentiment-time-party2.svg', format='svg')

# plt.close()
# plt.plot(zip(*repNegativeData).reverse(), label='dem')
# plt.plot(zip(*demNegativeData).reverse(), label='rep')
# plt.legend()
# plt.xlabel('Year')
# plt.ylabel('Proportion of words in  dictionaries')
# plt.title('Negative Sentiment over time in US democratic/republican election debates')
# plt.savefig('analysis-sentiment-time-party2.svg', format='svg')
