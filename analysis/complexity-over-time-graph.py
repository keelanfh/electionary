import json
import matplotlib.pyplot as plt
import os
from scipy import stats
import numpy
from commonfunctions import commonfunctions as cf

root_directory = os.path.dirname(os.path.abspath(os.curdir))

with open('complexity-over-time2.json', 'r') as f:
    results = json.load(f)

# The graph plots on the Y axis the relative amount of common nouns
# linr = stats.linregress(results[0], results[1])
# print stats.linregress(results[0], results[1])
# x = numpy.linspace(1960,2020,10)
# y = [linr.intercept + linr.slope * x_ for x_ in x]
# plt.plot(x,y)
# plt.plot(results[0], results[1], 'ro')
# plt.xlabel('Year')
# plt.ylabel('Common Nouns')
# plt.savefig(os.path.join(root_directory, 'images', 'complexity-over-time.svg'), format='svg')


plt.style.use('ggplot')
fig = plt.figure(0)
ax = fig.gca()
ax.grid(b=False)
ax.set_axis_bgcolor('white')

ax.plot(results[0], results[1], color='gray', lw=2.5)
ax.set_xlabel('Year')
ax.set_ylabel('Proportion of words in simple word dictionary')
ax.set_title('Occurrence of simple words in US presidential election campaigns', y=1.05)
plt.savefig(os.path.join(root_directory, 'images', 'analysis-complexity-time.svg'), format='svg')

print cf.generate_rawgit_img_embed(os.path.join('images', 'analysis-complexity-time.svg'))