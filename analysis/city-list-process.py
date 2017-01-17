import csv
import json

with open('worldcitiespop.txt', 'r') as f:
    csvr = csv.DictReader(f)
    cities = [x for x in csvr]


def remove_awkward_things(x):
    return {'City':x['City'],
            'Country': x['Country'],
            'Population': x['Population'],
            'Latitude': x['Latitude'],
            'Longitude': x['Longitude']}

cities = [remove_awkward_things(x) for x in cities if not x['Population'] == '']
cities = [x for x in cities if (int(x['Population']) > 100000)]
print "Halfway there... maybe..."

cities = sorted(cities, key=lambda x: int(x['Population']), reverse=True)

print len(cities)
big_cities = []
# x is number
for x, city in enumerate(cities):
    if not [True for bigger_city in cities[:x] if city['City'] == bigger_city['City']]:
        big_cities.append(city)

print len(big_cities)

with open('worldcitiesout.json', 'w') as f:
    json.dump(big_cities, f)