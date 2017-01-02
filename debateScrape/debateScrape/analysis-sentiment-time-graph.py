import matplotlib.pyplot as plt
import json

with open('analysis-sentiment-time.json', 'r') as f:
    data = json.load(f)

uniqueYears = data['uniqueYears']
uniquenegativewords = data['uniquenegativewords']
uniquepositivewords = data['uniquepositivewords']

plt.plot(uniqueYears, uniquenegativewords)
plt.plot(uniqueYears, uniquepositivewords)
plt.xlabel('Year')
plt.ylabel('Proportion of words in negative/positive dictionaries')
plt.title('Sentiment over time in US presidential election debates')
plt.savefig('analysis-sentiment-time.svg', format='svg')