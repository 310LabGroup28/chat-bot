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
	'wit$check_weather_condition' : gi.get_weather,
	'wit$get_temperature' : gi.get_temperature,
	'wit$get_time' : tc.getLocalTime
}

witIntentResponseFormats = {
	'get_distance' : rf.getDistanceFormat,
	'get_time_difference' : rf.getTimeDifferenceFormat,
	'get_time_zone' : rf.getTimezoneFormat,
	'point_of_interest' : rf.getPointOfInterestFormat,
	'wit$check_weather_condition' : rf.getWeatherFormat,
	'wit$get_temperature' : rf.getTemperatureFormat,
	'wit$get_time' : rf.getLocalTimeFormat
}

class ChatbotResponse(object):

	def getResponse(question):
		jsonData = wa.sendRequest(question)
		print(jsonData)

		response = ""

		intents = jsonData['intents']
		entities = jsonData['entities']
		traits = jsonData['traits']
			
		if len(intents) == 0:
			response = "I'm sorry, I didn't quite understand that. Try asking for help to see the scope of my functionality, or try asking another question."
		else:
			for intent in intents:
				#print(intent)
				intentName = intent['name']
				response += witIntentResponseFormats[intentName](witIntents[intentName](entities), entities)

		return response


print(ChatbotResponse.getResponse("What are some POIs in Kelowna?"))