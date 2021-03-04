import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")

# Reterieve all of the anchore tage
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))

