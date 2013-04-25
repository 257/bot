import urllib
from xml.etree import ElementTree as ET

def get():
	f = urllib.urlopen('http://freegeoip.net/xml/')
	geoipxml = f.read()
	f.close()
	root = ET.fromstring(geoipxml)
	for child in root.iter('Longitude'):
		geoloc = dict(longitude = child.text)
	for child in root.iter('Latitude'):
		geoloc.update(latitude = child.text)
	for child in root.iter('City'):
		geoloc.update(city = child.text)
	for child in root.iter('CountryName'):
		geoloc.update(country = child.text)
	for child in root.iter('RegionCode'):
		geoloc.update(province = child.text)
	for neighbor in root.iter('ZipCode'):
		geoloc.update(zipcode = neighbor.text)
	for neighbor in root.iter('Ip'):
		geoloc.update(ip = neighbor.text)

	return geoloc


