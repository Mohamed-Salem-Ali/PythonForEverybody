import urllib.request 
import urllib.parse as up
import json
import ssl

serviceurl1 = "http://python-data.dr-chuck.net/geojson?"
serviceurl2 = "http://py4e-data.dr-chuck.net/json?"
# This API only accepts the university in a list of its accepted ones.
# This API uses the same parameters (sensor and address) as the Google API.
# This API also has no rate limit so you can test as often as you like.
# If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

parms = dict()
parms['address'] = address
parms['key'] = 42
url = serviceurl2 + urllib.parse.urlencode(parms)

print("Retrieving ", url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
#data = ur.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)


print(json.dumps(js, indent=4))


place_id = js["results"][0]["place_id"]
print("Place id", place_id)
