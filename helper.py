import creative
import random
import auction
def buildForAdvertizer(creatives_number, advertizer_id, country = None):
		result = []
		for i in range(0, creatives_number):
			result.append(creative.Creative(i, advertizer_id, random.randint(0, 100), country))
		return result

def buildRandom(creatives_number):
	result = []
	adv_num = random.randint(1, creatives_number/10)
	counter = creatives_number
	for i in range(0, adv_num):
		a = random.randint(1, creatives_number - i)
		tmp = buildForAdvertizer(a, i, "TEST")
		result.append(tmp)
	return result

def main ():
	creatives = buildRandom(100)
	printList(creatives)
	print "---------------------------------------------------------------"
	a = auction.Auction("shit")
	res = a.perform(creatives, 6, "TEST")
	printList(res)
		
def printList(creatives):
	for i in range(0, len(creatives)):
		print creatives[i]
		
		