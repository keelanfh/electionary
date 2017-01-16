import json
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from scipy import stats
import numpy
import commonfunctions as cf

root_directory = os.path.dirname(os.path.abspath(os.curdir))

with open('complexity-over-time.json', 'r') as f:
    results = json.load(f)

# The graph plots on the Y axis the relative amount of common nouns

# This is optional code for linear regression information/lines
# linr = stats.linregress(results[0], results[1])
# print stats.linregress(results[0], results[1])
# x = numpy.linspace(1960,2020,10)
# y = [linr.intercept + linr.slope * x_ for x_ in x]

plt.style.use('ggplot')
fig = plt.figure(0)
ax = fig.gca()
ax.grid(b=False)
ax.set_axis_bgcolor('white')

ax.set_xlim([1956, 2020])
ax.set_xticks(xrange(1960, 2020, 8))

ax.plot(results[0], results[1], color='gray', lw=2.5)
ax.set_xlabel('Year')
ax.set_ylabel('Proportion of nouns in dictionary of 504 most common nouns')
ax.set_title('Occurrence of the most common 504 nouns in US presidential election campaigns',
             fontdict={'fontsize': 12,
                       'fontweight': mpl.rcParams['axes.titleweight'],
                       'verticalalignment': 'baseline',
                       'horizontalalignment': 'center'},
             y=1.05)

plt.savefig(os.path.join(root_directory, 'images', 'analysis-complexity-time.svg'), format='svg')

print cf.generate_rawgit_img_embed(os.path.join('images', 'analysis-complexity-time.svg'))
