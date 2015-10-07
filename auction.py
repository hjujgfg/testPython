import creative
class Auction(object):
	"""docstring for Auction"""
	def __init__(self, arg):
		super(Auction, self).__init__()
		self.arg = arg
	def test_method(self):
		c = creative.Creative(4, 5, 6, "shit")
		print c