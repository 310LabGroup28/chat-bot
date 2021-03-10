from ipregistry import IpregistryClient
from geopy.geocoders import Nominatim
import geopy.distance

class Location(object):

	def getLocation(place = None):
		if place is None or place == 'here' or place == 'me':
			client = IpregistryClient("fs9pbuwmnx5r2g")  
			ipInfo = client.lookup()
			#print(ipInfo)
			return(ipInfo.location.get("latitude"), ipInfo.location.get("longitude"))

		else:
			geolocator = Nominatim(user_agent="chatbot")
			location = geolocator.geocode(place)
			return (location.latitude, location.longitude)

	def distanceByLatLong(self, entities):
		places = entities['wit$location:location']
		place1Coords = self.getLocation(places[0]['value'])
		place2Coords = self.getLocation(places[1]['value'])

		return geopy.distance.distance(place1Coords, place2Coords).km