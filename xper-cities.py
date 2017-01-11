import csv

cityList = []

with open('us-cities.csv') as f:
    cities = csv.reader(f)
    for city in cities:
        if not city[1].isdigit():
            cityList.append(city[1])

del cityList[0]

for city in cityList:
    print city