import json
import os

import matplotlib.pyplot as plt

from commonfunctions import commonfunctions as cf

root_directory = os.path.abspath(os.path.dirname(os.path.abspath(os.curdir)))
directory = os.path.join(root_directory, cf.working_directory)

with open('sentiment-time.json', 'r') as f:
    data = json.load(f)

uniqueYears = data['uniqueYears']
uniquenegativewords = data['uniquenegativewords']
uniquepositivewords = data['uniquepositivewords']

colors = ['#d8b365', '#5ab4ac']

plt.style.use('ggplot')
fig = plt.figure(0)
ax = fig.gca()
ax.grid(b=False)
ax.set_axis_bgcolor('white')

ax.plot(uniqueYears, uniquepositivewords, label='positive', color=colors[1], lw=2.5)
ax.plot(uniqueYears, uniquenegativewords, label='negative', color=colors[0], lw=2.5)
ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Proportion of words in negative/positive dictionaries')
ax.set_title('Sentiment over time in US presidential election debates', y=1.05)
plt.savefig(os.path.join(root_directory, 'images', 'analysis-sentiment-time.svg'), format='svg')
