#HTML from the data files below, and parse the data, extracting
#numbers and compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ingore ssl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,"html.parser")

#Retrive all of the number 
sum = 0
tags = soup('span')
for tag in tags:
    print('TAG:',tag)
    print('URL:',tag.get('href'),None)
    print('contents:',tag.contents[0])
    sum += int(tag.contents[0])
    print('Attrs:',tag.attrs)
    
print(sum)