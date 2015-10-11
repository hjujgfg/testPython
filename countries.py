"""Module loads countries from json file with specific structure and returns list of Cou"""
import json
from pprint import pprint
def loadCountries(fname="countriesTest.json"):
	"""yolo"""
	with open(fname) as fileS:
		data = json.load(fileS)
	dicts = byteify(data["countries"])
	res = []
	for t in dicts:
		res.append(convert(t))
	return res

def convert(dictCountry):
	"""converts dict entry produced by loadCountries to Country object"""
	return Country(dictCountry['name'], dictCountry['code'])

def byteify(input):
	"""This is a code from stackoverflow, which converts my unicode strings from file"""
	if isinstance(input, dict):
		return {byteify(key):byteify(value) for key,value in input.iteritems()}
	elif isinstance(input, list):
		return [byteify(element) for element in input]
	elif isinstance(input, unicode):
		return input.encode('utf-8')
	else:
		return input
class Country(object):
	"""We will handle countries as objects"""
	def __init__(self, name, code):
		super(Country, self).__init__()
		self.name = name
		self.code = code	
	def __repr__(self):
		return "Name: " + self.name + " code: " + self.code	