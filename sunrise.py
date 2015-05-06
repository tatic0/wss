#!/usr/bin/env python

## this returns json data, the sunset and sunrise
## events are available for $TODAY
## http://api.openweathermap.org/data/2.5/weather?q=Massy,fr&mode=json&units=metric

import requests
import json


baseurl = "http://api.openweathermap.org/"
#url = baseurl + "data/2.5/weather?q=Massy,fr&mode=json&units=metric" ## id is recommended over city name
url = baseurl + "data/2.5/weather?id=2995206&mode=json&units=metric"

req = requests.post(url)
dldata = req.text

# json can be prettified with:
# wget "http://api.openweathermap.org/data/2.5/weather?q=Massy,fr&mode=json&units=metric" -O - | python -m json.tool

data = json.loads(dldata)
lastRequestTime = data['dt']
# debug
#now = 1430937778

sunrise = data['sys']['sunrise']
sunset= data['sys']['sunset']
dawn = sunrise - 1800

print(lastRequestTime)
print(dawn)
print(sunrise)
print(sunset)
if lastRequestTime < sunrise:
  print("Skies are dark, let's shoot the stars")
  if lastRequestTime > dawn:
    print("It's almost dawn, better stop doing long exposure")
if lastRequestTime < sunset:
  print("It's daytime, long exposure is useless")
