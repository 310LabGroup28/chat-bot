import json
from witapi import WitAPI as wa
from location import Location as lc
from responseformat import ResponseFormat as rf
from timechatbot import TimeChatbot as tc

witIntents = {
	'get_distance' : lc.distanceByLatLong,
	'get_time_zone' : tc.getTimezone,
	'wit$get_time' : tc.getLocalTime
}

witIntentResponseFormats = {
	'get_distance' : rf.getDistanceFormat,
	'get_time_zone' : rf.getTimezoneFormat,
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
			
		
		for intent in intents:
			#print(intent)
			intentName = intent['name']
			response += witIntentResponseFormats[intentName](witIntents[intentName](entities), entities)

		return response


print(ChatbotResponse.getResponse("What time is it in Kelowna? And what time is it in Vancouver?"))