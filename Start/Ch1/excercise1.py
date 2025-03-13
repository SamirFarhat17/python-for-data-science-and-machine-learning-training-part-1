# Python code​​​​​​‌‌​​‌‌‌​​‌‌‌​​​​‌‌‌​​​‌​‌ below
# Use print("messages...") to debug your solution.
import json

with open("../../sample-weather-history.json", "r") as weatherfile:
    weather_data = json.load(weatherfile)

def get_cold_windy_rainy_days(data):
    # your code goes here
    return list(filter(lambda d:is_rainy_cold_windy(d), data))

def is_rainy_cold_windy(day):
    return day['prcp'] > 0.7 and ((day['tmin'] + day['tmax'])/2 < 45) and day['awnd'] > 10

print(get_cold_windy_rainy_days(weather_data))
print(len(get_cold_windy_rainy_days(weather_data)))