# extract the href= vaues from the anchor tags, scan for a tag 
# that is in a particular position relative to the first name in 
# the list, follow that link and repeat the process a number of 
# times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Igonre ssl certificate error
ctx = ssl.create_default_context
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
cnt = int(input('Enter count: '))
ps = int(input('Enter position: '))-1
html = urllib.request.urlopen(url, context= ctx).read()
soup = BeautifulSoup(html, 'html.parser')
seq = list()
tags = soup('a')
print('Retrieving: ', url)

#Reterive name form the page

for i in range(cnt):
    link = tags[ps].get('href',None)
    print('Retrieving: ', link)
    seq.append(tags[ps].contents[0])
    html = urllib.request.urlopen(link, context= ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[ps].get('href', None)
    
print(seq[-1])