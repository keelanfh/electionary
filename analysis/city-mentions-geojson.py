import json

with open('city-mentions.json', 'r') as f:
    citymentions = json.load(f)

for citymention in citymentions:
    citymention['no_of_mentions'] = len([True for x in citymentions if citymention['city'] == x['city']])


def geojson(citymention):
    return {'type': 'Feature', 'geometry': {
        'type': 'Point',
        'coordinates': [float(citymention['city']['Longitude']), float(citymention['city']['Latitude'])]},
            'properties': {'title': ", ".join([citymention['speaker'], citymention['debate']['date']]),
                           'mentions': citymention['no_of_mentions'], 'city': citymention['city']['City']}}


def geojsontext(citymentions):
    citymentions = [{'mentions': x['no_of_mentions'], 'city': x['city']['City'].capitalize(),
                     'coordinates': [float(x['city']['Longitude']),
                                     float(x['city']['Latitude'])]} for x in citymentions]

    citymentions = [json.dumps(x) for x in citymentions]
    citymentions = set(citymentions)
    citymentions = [json.loads(x) for x in citymentions]

    return [{'type': 'Feature', 'geometry': {
        'type': 'Point',
        'coordinates': x['coordinates']},
             'properties': {'mentions': x['mentions'], 'city': x['city'] + " - " + str(x['mentions'])}} for x in citymentions]


geojsons = [geojson(x) for x in citymentions]
print geojsons

geojsons = {'type': 'FeatureCollection', 'features': geojsons}
print geojsons

with open('geo-jsons.json', 'w') as f:
    json.dump(geojsons, f)

geojsontext = {'type': 'FeatureCollection', 'features': geojsontext(citymentions)}

with open('geo-jsons-text.json', 'w') as f:
    json.dump(geojsontext, f)
