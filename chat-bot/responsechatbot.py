import json
from witapi import WitAPI as wa
from location import Location as lc
from responseformat import ResponseFormat as rf
from timechatbot import TimeChatbot as tc
from geoInfo import GeoInfo as gi


witIntents = {
	'get_distance' : lc.distanceByLatLong,
	'get_time_difference' : tc.getTimeDifference,	
	'get_time_zone' : tc.getTimezone,
	'point_of_interest' : gi.get_point_of_interest,
	'forecast' : gi.get_weather,
	'wit$get_temperature' : gi.get_temperature,
	'wit$get_time' : tc.getLocalTime
}

witIntentResponseFormats = {
	'get_distance' : rf.getDistanceFormat,
	'get_time_difference' : rf.getTimeDifferenceFormat,
	'get_time_zone' : rf.getTimezoneFormat,
	'point_of_interest' : rf.getPointOfInterestFormat,
	'forecast' : rf.getWeatherFormat,
	'wit$get_temperature' : rf.getTemperatureFormat,
	'wit$get_time' : rf.getLocalTimeFormat
}

class ChatbotResponse(object):

	def getResponse(question):
		jsonData = wa.sendRequest(question)
		#print(jsonData)

		response = ""

		intents = jsonData['intents']
		entities = jsonData['entities']
		traits = jsonData['traits']

		for trait in traits:
			if trait == 'wit$greetings':
				response += "Hello! I can help with things related to geographic data.\nTry asking me how far two places are from each other, or ask me about the weather somewhere.\nIf you want to know more about what I can do, try asking for help.\n"
			if trait == 'help':
				response += "I have a few things I can help you with.\nI can get the temperature at multiple locations, the weather forecast, and points of interest nearby.\nI can also tell you what the local time is for any location, and help calculate time differences between locations.\nLastly, I can measure distances between two locations in kilometers.\n"
			if trait == 'wit$bye':
				response += "Goodbye!"

		if len(intents) == 0 and len(traits) == 0:
			response = "I'm sorry, I didn't quite understand that. Try asking for help to see the scope of my functionality, or try asking another question."
		else:
			for intent in intents:
				#print(intent)
				intentName = intent['name']
				response += witIntentResponseFormats[intentName](witIntents[intentName](entities), entities)

		return response
