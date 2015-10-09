import json
from pprint import pprint
def loadCountries(fname):
	with open(fname) as fileS:
		data = json.load(fileS)
	pprint(data)
	return data["countries"]