class ResponseFormat(object):
	def getDistanceFormat(self, distance, entities):
		entities = entities['wit$location:location']
		place1 = entities[0]['value']
		if len(entities) == 1:
			return "The distance to " + place1 + " is " + str(distance) + "km."
		else:
			place2 = entities[1]['value']
			return "The distance between " + place1 + " and " + place2 + " is " + str(distance) + "km."

	def getTimezoneFormat(self, timezone, entities):
		entities = entities['wit$location:location']
		place = entities[0]['value']
		return "The time zone at " + place + " is " + timezone + "."

	def getLocalTimeFormat(self, time, entities):
		entities = entities['wit$location:location']
		response = ""
		i = 0
		for location in [entities[0]['value']]: # there may be some problems
			response += "The time in " + location + " is " + str(time[i]) + ".\n"
			i = i + 1
		return response

	def getTimeDifferenceFormat(self, time, entities):
		entities = entities['wit$location:location']
		if len(entities) == 1:
			return "The difference in time from here to " + entities[0]['value'] + " is " + str(time) + "."
		else:
			return "The difference in time between " + entities[0]['value'] + " and " + entities[1]['value'] + " is " + str(time) + "."

	def getTemperatureFormat(self, temps, entities):
		entities = entities['wit$location:location']
		response = ""
		i = 0
		for location in entities:
			response += "The temperature in " + location['value'] + " is " + str(temps[i]['temp']) + " degrees celcius.\n"
			i = i + 1
		return response

	def getWeatherFormat(self, weather, entities):
		entities = entities['wit$location:location']
		return "The weather in " + entities[0]['value'] + " is " + str(weather) + "."

	def getPointOfInterestFormat(self, POI, entities):
		entities = entities['wit$location:location']
		response = "The POIs in " + entities[0]['value'] + " are "
		for poi in POI:
			stringsplitpoint = poi.find(', ') + 2
			response += poi[stringsplitpoint:poi.find(',', stringsplitpoint+1)] + ", "
		response = response[:-2]
		response += "."
		return response

# test for this class:
"""
entities = {'entities': {'wit$location:location': [{'body': 'Kelowna',
    'confidence': 0.9962,
    'end': 39,
    'entities': [],
    'id': '184461976774247',
    'name': 'wit$location',
    'role': 'location',
    'start': 32,
    'suggested': True,
    'type': 'value',
    'value': 'Kelowna'}]},
 'intents': [{'confidence': 0.9459,
   'id': '1062561500902258',
   'name': 'forecast'}],
 'text': 'What is the weather forecast in Kelowna?',
 'traits': {}}
tmp = ResponseFormat()
print(tmp.getDistanceFormat(1000, entities['entities']))
print(tmp.getTimezoneFormat('Toronto timezone', entities['entities']))
time01 = ['06:06:00', '12:00:00','06:06:00', '12:00:00']
print(tmp.getLocalTimeFormat(time01, entities['entities']))
print(tmp.getTimeDifferenceFormat('1 day', entities['entities']))
temp01 = [{'feels_like': -7.35,
  'temp': -3.52,
  'temp_kf': None,
  'temp_max': -2.78,
  'temp_min': -4.0}]
#print(temp01)
print(tmp.getTemperatureFormat(temp01, entities['entities']))
print(tmp.getWeatherFormat('clear sky', entities['entities']))
poi01 = ['distance: 113, Kelowna Cruises, 238 Queensway, Kelowna, BC V1Y, Canada',
 'distance: 116, Hydrofly Kelowna, 230 Queensway, Kelowna, BC V1Y, Canada',
 'distance: 124, Kelownacruises - Lake, 239 Queensway, Kelowna, BC V1Y, Canada',
 'distance: 140, Okanagan Heritage Museum, 470 Queensway, Kelowna, BC V1Y, Canada',
 'distance: 140, Okanagan Heritage Museum, 470 Queensway, Kelowna, BC V1Y, Canada']
#print(poi01)
print(tmp.getPointOfInterestFormat(poi01, entities['entities']))
"""
