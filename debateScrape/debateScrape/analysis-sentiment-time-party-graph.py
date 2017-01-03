import matplotlib.pyplot as plt
import json

# TODO name of the Y axis has to be changed and a legend has to be added

with open('analysis-sentiment-time-party.json', 'r') as f:
    data = json.load(f)

r, d = None, None

for datum in data:
    if datum['party'] == 'r':
        r = datum
    if datum['party'] == 'd':
        d = datum

uniqueDemYears = d['uniqueYears']
uniqueDemNegativeWords = d['uniquenegativewords']
uniqueDemPositiveWords = d['uniquepositivewords']
uniqueRepYears = r['uniqueYears']
uniqueRepNegativeWords = r['uniquenegativewords']
uniqueRepPositiveWords = r['uniquepositivewords']


plt.plot(uniqueRepYears, uniqueRepPositiveWords, label='dem')
plt.plot(uniqueDemYears, uniqueDemPositiveWords, label='rep')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Proportion of words in  dictionaries')
plt.title('Positive Sentiment over time in US democratic/republican election debates')
plt.savefig('analysis-sentiment-time-party.svg', format='svg')

plt.close()
plt.plot(uniqueRepYears, uniqueDemNegativeWords, label='dem')
plt.plot(uniqueDemYears, uniqueRepNegativeWords, label='rep')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Proportion of words in  dictionaries')
plt.title('Negative Sentiment over time in US democratic/republican election debates')
plt.savefig('analysis-sentiment-time-party2.svg', format='svg')
