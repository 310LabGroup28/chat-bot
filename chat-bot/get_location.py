from ipregistry import IpregistryClient

def getLocation():
	client = IpregistryClient("tryout")  
	ipInfo = client.lookup() 
	return ipInfo.location