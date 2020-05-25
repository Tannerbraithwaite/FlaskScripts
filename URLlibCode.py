import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

req= urllib.request.urlopen('https://www.google.com')
print(req.read())
url = 'https://www.google.com/search'
value ={'q':'Your Google Search'}
data = urllib.parse.urlencode(value)

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

# data = data.encode('utf-8')
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
resp_data = response.read()

print(resp_data)
