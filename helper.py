import creative
import random
def buildForAdvertizer(creatives_number, advertizer_id, country = None):
		result = []
		for i in range(0, creatives_number):
			result.append(creative.Creative(i, advertizer_id, random.randint(0, 100), country))
		return result
		
def printList(creatives):
	for i in range(0, len(creatives)):
		print creatives[i]
		
		