from ipregistry import IpregistryClient
from geopy.geocoders import Nominatim
import geopy.distance

class Location(object):
	def getLocation(self, place = None):
		if place is None:
			client = IpregistryClient("fs9pbuwmnx5r2g")  
			ipInfo = client.lookup()
			#print(ipInfo)
			return(ipInfo.location.get("latitude"), ipInfo.location.get("longitude"))
		else:
			geolocator = Nominatim(user_agent="chatbot")
			location = geolocator.geocode(place)
			return (location.latitude, location.longitude)

	def distanceByLatLong(self, lat1, long1, lat2 = None, long2 = None):
		if lat2 is None:
			coord1 = (lat1, long1)
			coord2 = self.getLocation()
		else:
			coord1 = (lat1, long1)
			coord2 = (lat2, long2)

		return geopy.distance.distance(coord1, coord2).km
