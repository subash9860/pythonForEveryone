
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse 
# and extract the comment counts from the JSON data, compute the sum of the numbers in the file 
# and enter the sum below:
# We provide two files for this assignment. One is a sample file where we give you the sum for your
# testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1166287.json (Sum ends with 47)

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
