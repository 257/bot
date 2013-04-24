#!/usr/bin/python
import urllib
#import requests
f = urllib.urlopen('http://api.hostip.info/')
yourxml = f.read()
f.close()
import xml.etree
from xml.etree import ElementTree as ET
#print ET.fromstring(yourxml).find('//Hostip/{http://opengis.net.gml}name').text
root = ET.fromstring(yourxml)
#print root.findall("Hostip")
for child in root:
	for cchild in child:
		for yachild in cchild:
			print yachild.tag, yachild.attrib
