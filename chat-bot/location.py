from geopy.geocoders import Nominatim
from geopy import distance
import ipregistry


class Location(object):

	def getLocation(place = None):
		if place is None or place == 'here' or place == 'me':
			client = ipregistry.IpregistryClient("fs9pbuwmnx5r2g", cache=ipregistry.DefaultCache(maxsize=2048, ttl=600))  
			ipInfo = client.lookup()
			#print(ipInfo)
			return(ipInfo.location.get("latitude"), ipInfo.location.get("longitude"))

		else:
			geolocator = Nominatim(user_agent="chatbot")
			location = geolocator.geocode(place)
			return (location.latitude, location.longitude)

	def distanceByLatLong(entities):
		places = entities['wit$location:location']
		place1Coords = Location.getLocation(places[0]['value'])
		if len(places) == 1:
			place2Coords = Location.getLocation()
		else:
			place2Coords = Location.getLocation(places[1]['value'])

		return distance.distance(place1Coords, place2Coords).km