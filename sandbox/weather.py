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
#for child in root:
#	print child.tag, child.attrib
#	for cchild in child:
#		print cchild.tag, cchild.attrib
#		for yachild in cchild:
#			print yachild.tag, yachild.attrib
#			for yac in yachild:
#				print yac.tag, yac.attrib

#print root[1].tag
#for neighbor in root.iter():
#	print neighbor.text
for neighbor in root.iter('countryName'):
	geoloc = dict(country = neighbor.text)
for child in root.iter('ip'):
	dict(ip = child.text)
for child in root[3].iter('{http://www.opengis.net/gml}name'):
	city = child.text
for child in root.iter('{http://www.opengis.net/gml}coordinates'):
	coor = child.text

print geoloc
