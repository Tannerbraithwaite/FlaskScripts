from bs4 import BeautifulSoup
import time
import urllib.request
from MYSQLConnection import connection

req = urllib.request.urlopen('http://www.nationjournal.com/politics?rss=1')

xml = BeautifulSoup(req, 'xml')

def parse_links():
    for item in xml.finadAll('link')[3:]:
        url=item.text
        c.execute("SELECT * FROM links WHERE link = (%s)", (url))
        rows = c.fetchall()
        if len(rows)==0:
            c.execute("INSERT INTO links  (time, link) VALUES (%s, %s)", (time.time(), link))
            conn.commit()
        time.sleep(10)
    conn.closer()

while True:
    parse_links():
