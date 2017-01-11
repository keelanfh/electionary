import json
import matplotlib.pyplot as plt
import os
import debateScrape.debateScrape.commonfunctions as cf

with open('analysis-complexity-over-time.json', 'r') as f:
    results = json.load(f)

# The graph plots on the Y axis the relative amount of common nouns

plt.plot(results[0], results[1], 'ro')
plt.xlabel('Year')
plt.ylabel('Common Nouns')
plt.savefig(os.path.join(cf.root_directory, 'images', 'complexity-over-time.svg'), format='svg')