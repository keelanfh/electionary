import json
import matplotlib.pyplot as plt

with open('analysis-complexity-over-time.json', 'r') as f:
    results = json.load(f)

# The graph plots on the Y axis the relative amount of common nouns

plt.plot(results[0], results[1], 'ro')
plt.xlabel('Year')
plt.ylabel('Common Nouns')
plt.savefig('images/analysis-complexity-time.svg', format='svg')