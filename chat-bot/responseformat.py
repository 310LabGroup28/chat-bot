

class ResponseFormat(object):
	def getDistanceFormat(distance, entities):
		entities = entities['wit$location:location']
		place1 = entities[0]['value']
		if len(entities) == 1:
			return "The distance to " + place1 + " is " + str(distance) + "km."
		else:
			place2 = entities[1]['value']
			return "The distance between " + place1 + " and " + place2 + " is " + str(distance) + "km."

	def getTimezoneFormat(timezone, entities):
		entities = entities['wit$location:location']
		place = entities[0]['value']
		return "The time zone at " + place + " is " + timezone + "."

	def getLocalTimeFormat(time, entities):
		entities = entities['wit$location:location']
		response = ""
		i = 0
		for location in entities:
			response += "The time in " + location['value'] + " is " + str(time[i]) + ".\n"
			i = i + 1
		return response