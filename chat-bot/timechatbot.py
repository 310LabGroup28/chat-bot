from lib.timezonefinder import TimezoneFinder
from datetime import datetime
from location import Location as lc
from lib import pytz

class TimeChatbot(object):

	def getTimezone(entities):
		entities = entities['wit$location:location']
		timezones = []
		for location in entities:
			coords = lc.getLocation(location['value'])
			latitude = coords[0]
			longitude = coords[1]
			tf = TimezoneFinder()
			timezones.append(tf.timezone_at(lng=longitude, lat=latitude))

		return timezones

	def getLocalTime(entities):
		locationEntities = entities['wit$location:location']
		dateTime = [] 
		if len(locationEntities) == 0:
			dateTime.append(datetime.now())
		else:
			timezoneList = TimeChatbot.getTimezone(entities)
			for timezone in timezoneList:
				tz = pytz.timezone(timezone)
				dateTime.append(datetime.now(tz))
	
		return dateTime