import json
import commonfunctions as cf
import datetime as dt
import matplotlib.pyplot as plt

with open('realDonaldTrumpTweetsResults.json', 'r') as f:
    statuses = json.load(f)

results = {}
for status in statuses:
    month = cf.iso_to_datetime(status['date']).month
    year = cf.iso_to_datetime(status['date']).year
    if year == 2016:
        if month not in results:
            results[month] = [status]
        else:
            results[month].append(status)

positive_results = [(month_results, cf.mean([status['total_pos_words'] for status in results[month_results]]))
       for month_results in results]
negative_results = [(month_results, cf.mean([status['total_neg_words'] for status in results[month_results]]))
       for month_results in results]
print positive_results
print negative_results

plt.figure(0)
labels = ['Positive', 'Negative']
for labelno, data in enumerate([positive_results, negative_results]):
    data2 = zip(*data)
    plt.plot(data2[0], data2[1], label=labels[labelno])

plt.legend()
plt.xlabel('month')
plt.ylabel('Proportion of words in  dictionaries')
plt.title('Negative Sentiment over time in US democratic/republican election debates')
plt.savefig('twitter-analysis-sentiment-time-party.svg', format='svg')
