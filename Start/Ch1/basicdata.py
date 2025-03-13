# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
max = -237
for d in weatherdata:
    if(d['tmax'] > max):
        max = d['tmax']
print(max)

# TODO: What was the coldest day in the data set?
min = 237
for d in weatherdata:
    if(d['tmin'] < min):
        min = d['tmin']
print(min)

# TODO: How many days had snowfall?
count = 0
for d in weatherdata:
    if(d['snow'] > 0.0):
        count += 1
print(count)
