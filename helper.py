import creative
import random
import auction
import countries
countriesList = []
def buildForAdvertizer(creatives_number, advertizer_id, country = None):
	"""build a list of cratives for an advertizer"""
	result = []
	
	for i in range(0, creatives_number):
		if country is not None:
			local_country = country
		else: 
			local_country = countriesList[random.randint(0, 10)].code
		result.append(creative.Creative(i, advertizer_id, random.randint(0, 100), local_country))
	return result

def buildRandom(creatives_number, country=None):
	"""build a list of creatives with given length, but with random number of advertizers and also random number of cratives for an advertizer"""
	result = []
	adv_num = random.randint(1, creatives_number/10)
	counter = creatives_number
	slots = creatives_number
	global countriesList
	countriesList = countries.loadCountries()
	for i in range(0, adv_num):
		a = random.randint(1, (slots - (adv_num - i)))
		if i == adv_num - 1:
			a = slots
		else: 
			slots -= a
		#print "advertizer: " + str(i) + " expected num: " + str(a) 
		#if country is not None:
		#	local_country = country
		#else: 
		#	local_country = countriesList[random.randint(0, 243)].code
		tmp = buildForAdvertizer(a, i)
		result.extend(tmp)
	return result

def main ():
	creatives = buildRandom(100)
	printList(creatives)
	print "---------------------------------------------------------------"
	a = auction.Auction("shit")
	res = a.perform(creatives, 6, "TEST")
	printList(res)
		
def printList(creatives):
	for i in creatives:
		print i
		
		