# Example file for Advanced Python: Hands On by Joe Marini
# Load and parse a JSON data file and determine some information about it

import json

# TODO: open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weather_file:
  weather_data = json.load(weather_file)

# TODO: make sure the data loaded correctly by printing the length of the dataset
print(len(weather_data))

# TODO: let's also take a look at the first item in the data
print(weather_data[0])

# TODO: How many days of data do we have for each year?
years = {}

for d in weather_data:
  key = d['date'][0:4]
  if key in years:
    years[key] += 1
  else:
    years[key] = 1

print(years)
