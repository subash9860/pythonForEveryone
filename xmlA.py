import urllib.request, urllib.parse, urllib.error as ur
import xml.etree.ElementTree as ET 
import ssl

ctx = ssl.create_default_context() 
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

c =0 
sum =0
address = input('Enter location:')
uh = urllib.request.urlopen(address , context= ctx)
    
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')
for item in counts:
    sum += int(item.text)
    c += 1

print('Count: ',c)
print('Sum: ',sum)