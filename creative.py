
class Creative(object):
	"""Model of a creative item"""
	def __init__(self, ID, advertizer_id, cost, country=None):
		super(Creative, self).__init__()
		self.ID = ID
		self.advertizer_id = advertizer_id
		self.cost = cost
		if country is not None:
		    self.country = country
 	def __repr__(self):
 		return "ID: " + str(self.ID) + " adv_id: " + str(self.advertizer_id) \
		 + " cost: " + str(self.cost) + str(self.country)