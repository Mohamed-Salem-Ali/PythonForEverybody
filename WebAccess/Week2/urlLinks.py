import urllib.request
from bs4 import BeautifulSoup
import ssl

#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname =False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the anchor tags 
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

# import urllib.request , urllib.parse , urllib.error
# x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# print(type(x))