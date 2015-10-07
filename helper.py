import creative
import random
def buildForAdvertizer(creatives_number, advertizer_id, country = None):
		result = []
		for i in range(1, creatives_number):
			result.append(creative.Creative(i, advertizer_id, random.randint(0, 100), country))
		return result
		
def printList(creatives):
	for i in range(len(creatives)):
		print creatives[i]

class AuctionHelper(object):
	"""AuctionHelper contains utilites for quicker creation of 
		creative lists"""
	def __init__(self, arg):
		super(AuctionHelper, self).__init__()
		self.arg = arg
	
		