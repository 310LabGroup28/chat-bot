from datetime import datetime
from datetime import timedelta
import json 
import requests

URL = "https://api.wit.ai/message"
API_KEY = "6LLX376UX4FWFSX5KVNLSRPCXSECLGXE"
headers  = {
	"Authorization" : "Bearer " + API_KEY
}

class WitAPI(object):

	def sendRequest(question):
		date = datetime.now()
		date = date.strftime("%Y%m%d")
		resp = requests.get(URL + "?v=" + date + "&q=" + question, headers = headers)

		if resp.status_code != 200:
		    print('error: ' + str(resp.status_code))
		    return None
		else:
		    print('Success')
		    return resp.json()