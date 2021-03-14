# The program will prompt for a location, contact a web service and retrieve 
# JSON for the web service and parse that data, and retrieve the first place_id 
# from the JSON. A place ID is a textual identifier that uniquely identifies 
# a place as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key= False 
 
if api_key is False:
    api_key= 42
    serviceurl= 'http://py4e-data.dr-chuck.net/json?'
    
ctx = ssl.create_default_context
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location:')
parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)
place_id = js['results'][0]['place_id']
print(place_id)