
import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

c =0 
sum =0
address = input('Enter location:')
print('Retrieving',address)
uh = urllib.request.urlopen(address , context= ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
for item in info['comments']:
    sum += int(item['count'])
    c += 1

print('Count: ',c)
print('Sum: ',sum)
