import creative
import random
class Auction(object):
	"""This is a class for auction proccess"""
	def __init__(self):
		super(Auction, self).__init__()

	def perform (self, creatives, num_winners, country=None):
		cr = sorted(creatives, key=lambda c: c.cost, reverse=True)
		filtered = []
		#filter by country and take only one most valuable creative from each advertizer as we have to return items with unique advertizer id
		advertizers = set() 
		for c in cr: 
			if hasattr(c, 'country') and country is not None and c.country==country or not hasattr(c, 'country'):
				if c.advertizer_id not in advertizers:
					advertizers.add(c.advertizer_id)
					filtered.append(c)
		if len(filtered) <= num_winners:
			return filtered
		slots = num_winners
		result = []
		#we go through filtered values and append creatives with the highest cost or take random from clusters with same cost or add the whole cluster 
		for i in range(0, len(filtered)):
			if slots == 0:
				break
			if filtered[i].cost != filtered[i+1].cost:
				result.append(filtered[i])
				slots -= 1
			else: 
				cluster = []
				tCost = filtered[i].cost
				while filtered[i].cost == tCost and i < len(filtered):
					cluster.append(filtered[i])
				if len(cluster) <= slots:
					result.append(cluster)
					slots -= len(cluster)
				else:
					#we want to cover all slots
					bound = slots 
					for k in range(0, bound):
						randIndex = random.randint(0, len(cluster))
						result.append(cluster[randIndex])
						#actually it is not necessary but for consistency... 
						slots -= 1 
						#is it honest to decrease set size? we'll find out in tests  
						cluster.remove(cluster[randIndex])