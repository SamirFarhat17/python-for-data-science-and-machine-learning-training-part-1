# Python code​​​​​​‌‌​​‌‌‌​​‌‌‌​​​‌​​‌​​‌​​​ below
# Use print("messages...") to debug your solution.

import json
import pprint

def get_day_temp_descriptions():
   # Your code goes here
    with open("../../sample-weather-history.json", "r") as weatherfile:
      weather_data = json.load(weatherfile)

    desc = list(map(lambda d:get_tuple(d), weather_data))
      
    return desc

def get_tuple(day):
  temp = (day['tmax'] + day["tmin"])/2
  temp_cat = ""

  if(temp <= 60): 
    temp_cat = "cold"
  elif(temp >= 80): 
    temp_cat = "hot"
  else:
    temp_cat = "warm"

  return (day['date'],temp_cat)


pprint.pp(get_day_temp_descriptions())