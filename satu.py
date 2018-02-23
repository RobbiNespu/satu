#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup

url = "http://www.satuwater.com.my/akauns.php" 

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page,"lxml")

for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')
    print tds[0].text
    #print " %s, %s,%s" % \
    #      (tds[0].text, tds[1].text, tds[2].text)
