# Example file for Advanced Python: Hands On by Joe Marini
# Transform data from one format to another

import json
import copy
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the map() function is used to transform data from one form to another
# TODO: Let's convert the weather data from imperial to metric units
def ToC(f):
    f = 0 if f is None else f
    return (f - 32) * 5/9


def ToCM(i):
    i = 0 if i is None else i
    return i * 2.54


def ToKPH(s):
    s = 0 if s is None else s
    return s * 1.60934


def ToMetric(wd):
    new_wd = copy.copy(wd)
    new_wd['tmin'] = ToC(wd['tmin'])
    new_wd['tmax'] = ToC(wd['tmax'])
    new_wd['awnd'] = ToKPH(wd['awnd'])
    new_wd['prcp'] = ToCM(wd['prcp'])
    new_wd['snow'] = ToCM(wd['snow'])
    new_wd['snwd'] = ToCM(wd['snwd'])
    return new_wd


# TODO: Use map() to call ToMetric and convert weatherdata to metric
metric_weather = list(map(ToMetric, weatherdata))
pprint.pp(weatherdata[0])
pprint.pp(metric_weather[0])

# TODO: use the map() function to convert objects to tuples
# in this case, create tuples with a date and the average of tmin and tmax
Avg_Temp = lambda t1, t2: (t1 + t2) / 2.0
