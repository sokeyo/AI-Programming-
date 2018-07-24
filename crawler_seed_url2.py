import urllib
from urllib import request
import urllib.parse
import re

#def test_method():

url = 'https://www.dndi.org'

values = {'s': 'basics', 'submit': 'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

# print (respData)
paragraphs = re.findall(r'<.*?>', str(respData))

for eachP in paragraphs:
    print(eachP)