from geopy.geocoders import Nominatim
from geopy import distance
import ipregistry

# in the scope of chatbot responses, the Location class is solely responsible for distanceByLatLong. 
# getLocation is a helper function because many of the requests require lat/long coords
class Location(object):

	#takes in a place as a string, returns a tuple containing lat/long coords (lat, long)
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

	# takes in a list of entities, returns the distance between the first two
	# if there is only one entity it returns the distance between your ip and that entity
	def distanceByLatLong(entities):
		if len(entities) > 0:
			places = entities['wit$location:location']
			place1Coords = Location.getLocation(places[0]['value'])
			if len(places) == 1:
				place2Coords = Location.getLocation()
			else:
				place2Coords = Location.getLocation(places[1]['value'])

			return distance.distance(place1Coords, place2Coords).km

		else:
			return 0