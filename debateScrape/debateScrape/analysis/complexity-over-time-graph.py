import json
import matplotlib.pyplot as plt
import os

root_directory = os.path.dirname(os.path.abspath(os.curdir))

with open('complexity-over-time.json', 'r') as f:
    results = json.load(f)

# The graph plots on the Y axis the relative amount of common nouns

plt.plot(results[0], results[1], 'ro')
plt.xlabel('Year')
plt.ylabel('Common Nouns')
plt.savefig(os.path.join(root_directory, 'images', 'complexity-over-time.svg'), format='svg')