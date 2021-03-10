from lib.timezonefinder import TimezoneFinder
from datetime import datetime
from location import Location as lc
from lib import pytz

class TimeChatbot(object):

	def getTimezone(entities, place = None):
		if place is None:
			timezones = []
			entities = entities['wit$location:location']
			for location in entities:
				coords = lc.getLocation(location['value'])
				latitude = coords[0]
				longitude = coords[1]
				tf = TimezoneFinder()
				timezones.append(tf.timezone_at(lng=longitude, lat=latitude))
			return timezones
		else:
			coords = lc.getLocation(place)
			latitude = coords[0]
			longitude = coords[1]
			tf = TimezoneFinder()
			return tf.timezone_at(lng=longitude, lat=latitude)

	def getLocalTime(entities, place = None):
		locationEntities = entities['wit$location:location']
		if place is None:
			dateTime = [] 
			if len(locationEntities) == 0:
				dateTime.append(datetime.now())
			else:
				timezoneList = TimeChatbot.getTimezone(entities)
				for timezone in timezoneList:
					tz = pytz.timezone(timezone)
					dateTime.append(datetime.now(tz))
			return dateTime
		else:
			timezone = TimeChatbot.getTimezone(entities, place)
			tz = pytz.timezone(timezone)
			return datetime.now(tz)

	def getTimeDifference(entities):
		times = TimeChatbot.getLocalTime(entities)
		if len(times) == 1:
			times.append(TimeChatbot.getLocalTime(entities, "here"))

		return times[0] - times[1]