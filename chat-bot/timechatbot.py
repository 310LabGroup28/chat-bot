from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

class TimeChatbot(object):

	def getTimezone(latitude, longitude):
		tf = TimezoneFinder()
		return tf.timezone_at(lng=longitude, lat=latitude)

	def getLocalTime(timeZone = None):
		if timeZone is None:
			dateTime = datetime.now()
		else:
			tz = pytz.timezone(timeZone)
			dateTime = datetime.now(tz)
		
		return dateTime