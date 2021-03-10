#you should install the package firstly
#!pip install pyowm 
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import json 
import requests

  # you should go to this URL: https://home.openweathermap.org/api_keys
  # to create your own key if you want to use this API
  # more info about this API: https://openweathermap.org/api/one-call-api
  api_key = "817d0ac612d439a9fe94c38f889fab28"
  owm = OWM(api_key)
  mgr = owm.weather_manager()

class GeoInfo(object):


  def __init__(self, lat=43.6532, long=-79.3832):
    self.lat = lat
    self.long = long
    self.observation = mgr.weather_at_coords(self.lat, self.long)
    self.w = self.observation.weather
  
  def get_temperature(self, lat=None, long=None, wtype='celsius'):
    if lat is not None and long is not None:
      self.lat = lat
      self.long = long
    self.observation = mgr.weather_at_coords(self.lat, self.long)
    self.w = self.observation.weather
    # print(w.temperature('celsius'))
    # w.to_dict()
    return self.w.temperature(wtype)
  '''
  def get_temperature(self, name='Toronto'):
    observation = mgr.weather_at_place(name)
    w = observation.weather
    print(w.temperature('celsius'))
    return w.to_dict()
  '''

  def get_weather(self):
    return self.w.detailed_status
  
  # limit, how many POIs you want to retrieve
  def get_point_of_interest(self, limit=5):
    URL = "https://discover.search.hereapi.com/v1/discover"
    latitude = self.lat
    longitude = self.long
    # get your key from developer.here.com
    poi_key = 'IIlHrKDojjhW90OB3KCEp6Xu0l8FX13NAdgFxMx4HbM' 
    query = 'tourist attractions'
    #print(latitude, longitude)
    PARAMS = {
          'apikey':poi_key,
          'q':query,
          'limit': limit,
          'at':'{},{}'.format(latitude,longitude)
          } 
    # sending request and getting the response as JSON
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()
    items = data['items']
    attractions = []
    # parse retrieved attractions data
    for it in items:
      att = 'distance: ' + str(it['distance']) + ', ' + it['address']['label']
      attractions.append(att)
    return attractions

# test
geoInfo = GeoInfo(22.2793278, 114.1628131)
# 43.6532, -79.3832 - Toronto / the default lat and long
# 51.5073219, -0.1276474 - London
# 40.7127281, -74.0060152 - New York
# 22.2793278, 114.1628131 - Hong Kong
# 39.906217, 116.3912757 - Beijing

temp = geoInfo.get_temperature()
wth = geoInfo.get_weather()
poi = geoInfo.get_point_of_interest(3)

print('temperature: ', temp)
print('weather: ', wth)
print('POI: ', poi)
