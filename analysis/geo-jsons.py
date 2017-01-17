import json
import numpy as np

with open('geo-jsons.json', 'r') as f:
    opened = json.load(f)
opened = opened['features']
opened = [{'mentions': x['properties']['mentions'], 'city': x['properties']['city']} for x in opened]
opened = [json.dumps(x) for x in opened]
opened = set(opened)
opened = [json.loads(x) for x in opened]
opened = sorted(opened, key=lambda x: x['mentions'], reverse=True)
for x in opened:
    print x
numbers = [x['mentions'] for x in opened]

print [np.percentile(numbers, x) for x in [0,20,40,60,80,100]]