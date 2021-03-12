#you should install the package firstly
#!pip install pyowm 
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import json 
import requests
from location import Location as lc

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
  
  def get_temperature(entities, lat=None, long=None, wtype='celsius'):
    if len(entities) != 0:
      locationEntities = entities['wit$location:location']
      #timeEntities = entities['wit$datetime:datetime']
    temps = []
    if len(entities) == 0:
      coords = lc.getLocation()
      lat = coords[0]
      long = coords[1]
      temps.append(mgr.weather_at_coords(lat, long).weather.temperature(wtype))
    else:
      for location in locationEntities:
        coords = lc.getLocation(location['value'])
        lat = coords[0]
        long = coords[1]
        temps.append(mgr.weather_at_coords(lat, long).weather.temperature(wtype))
    #observation = mgr.weather_at_coords(lat, long)
    #w = observation.weather
    # print(w.temperature('celsius'))
    # w.to_dict()
    return temps
  '''
  def get_temperature(self, name='Toronto'):
    observation = mgr.weather_at_place(name)
    w = observation.weather
    print(w.temperature('celsius'))
    return w.to_dict()
  '''

  def get_weather(entities, lat = 0, long = 0):
    locationEntities = entities['wit$location:location']
    if len(locationEntities) == 0:
      coords = lc.getLocation()
      lat = coords[0]
      long = coords[1]
    else:
      coords = lc.getLocation(locationEntities[0]['value'])
      lat = coords[0]
      long = coords[1]
    return mgr.weather_at_coords(lat, long).weather.detailed_status
  
  # limit, how many POIs you want to retrieve
  def get_point_of_interest(entities, limit=5, latitude = 0, longitude = 0):
    URL = "https://discover.search.hereapi.com/v1/discover"
    locationEntities = entities['wit$location:location']
    if len(locationEntities) == 0:
      coords = lc.getLocation()
      latitude = coords[0]
      longitude = coords[1]
    else:
      coords = lc.getLocation(locationEntities[0]['value'])
      latitude = coords[0]
      longitude = coords[1]
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
