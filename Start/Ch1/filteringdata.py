# Example file for Advanced Python: Hands On by Joe Marini
# Filter values out of a data set based on some criteria

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the filter() function gives us a way to remove unwanted data points
# TODO: create a subset of the data for days that had snowfall
snow_days = list(filter(lambda d :d['snow'] > 0, weatherdata))
print(len(snow_days))

# TODO: pretty-print the resulting data set
#pprint.pp(snow_days)

# filter can also be used on non-numerical data, like strings
# TODO: create a subset that contains summer days with heavy rain (more than 1 in, about 2.5cm)
def summer_rain_days(data):
    summer_rain_days = list(filter(lambda d:is_summer(d) and d['prcp'] >= 1, data))
    pprint.pp(summer_rain_days)
    print(len(summer_rain_days))

def is_summer(d):
    return d['date'][6] == '7' or d['date'][6] == '8'

summer_rain_days(weatherdata)