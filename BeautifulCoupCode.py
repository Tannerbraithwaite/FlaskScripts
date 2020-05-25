from bs4 import BeautifulSoup
import urllib.request
import time

req = urllib.request.urlopen('https://www.cnn.com')
xml = BeautifulSoup(req, features='lxml')
links = xml.findAll('link')
print(links)
print(links[0].text)
# for item in xml.findALL('link'):
#     url = item.text
#     news = urllib.request.urlopen(url).read()
#
#     page = BeautifulSoup(news)
#     for p in page.findALL('p'):
#         print(p.text)
#
#     time.sleep(10)
