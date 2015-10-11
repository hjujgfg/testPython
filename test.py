import unittest 
import helper
import countries
import creative
import auction

cList = []

def prepareCreatives():
	creatives = []
	global cList 
	cList = countries.loadCountries()

class testAuction(unittest.TestCase): 
	def test_simple(self):
		global cList
		helper.printList(cList)
		cr = [] 
		cr.append(creative.Creative(1, "adv1", 100))
		cr.append(creative.Creative(2, "adv1", 200, "country"))
		cr.append(creative.Creative(3, "adv2", 120))
		cr.append(creative.Creative(4, "adv2", 100, "country2"))
		cr.append(creative.Creative(5, "adv2", 100, "country3"))
		cr.append(creative.Creative(6, "adv3", 50, "country"))
		cr.append(creative.Creative(7, "adv3", 99))
		cr.append(creative.Creative(8, "adv3", 98))
		cr.append(creative.Creative(9, "adv4", 80))
		cr.append(creative.Creative(10, "adv4", 90))
		a = auction.Auction()
		res = a.perform(cr, 5, "country")
		helper.printList(res)
		correct_ids = [2, 3, 7, 10]
		self.assertTrue(len(res) == 4)
		x = 0
		for i in correct_ids:
			self.assertEqual(res[x].ID, i)
			x += 1
	def test_uniqueAdvertizer(self):
		pass

	def test_distribution100(self):
		creatives = helper.buildRandom(100)
		print "test 3 creatives list!"
		helper.printList(creatives)
		a = auction.Auction()
		dict = {}
		for i in range(100):
			#print "iteration: " + str(i)
			res = a.perform(creatives, 10, "AS")
			print res
			for c in res: 
				#dict [str(c)] += 1
				dict[str(c.ID)+str(c.advertizer_id)]
			#print dict

if __name__ == '__main__':
	prepareCreatives()
	unittest.main()