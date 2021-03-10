from timezonefinder import TimezoneFinder
from datetime import datetime
from location import Location as lc
import pytz

class TimeChatbot(object):

	def getTimezone(self, entities):
		entities = entities['wit$location:location']
		timezones = []
		for location in entities:
			coords = lc.getLocation(location['value'])
			latitude = coords[0]
			longitude = coords[1]
			tf = TimezoneFinder()
			timezones.append(tf.timezone_at(lng=longitude, lat=latitude))

		return timezones

	def getLocalTime(self, entities):
		locationEntities = entities['wit$location:location']
		dateTime = [] 
		if len(locationEntities) == 0:
			dateTime.append(datetime.now())
		else:
			timezoneList = self.getTimezone(self, entities)
			for timezone in timezoneList:
				tz = pytz.timezone(timezone)
				dateTime.append(datetime.now(tz))
	
		return dateTime