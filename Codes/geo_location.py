
#  Add the plus_code function to the geo_location.py file. The plus_code function takes a location string as input and returns the corresponding plus code using the Geoapify API. The function constructs the API request URL, sends the request, and parses the response to extract the plus code. If the location is not found or there is an error in the response, the function returns None.

import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    address = input('Enter location: ')
    if len(address) < 1: break


    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))


    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    # print(json.dumps(js, indent=4))
    plus_code = js['features'][0]['properties']['plus_code']
    print('Plus Code:', plus_code)
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted']
    print(location)




