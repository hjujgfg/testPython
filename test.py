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
		print "TEST test_simple init___________________________"
		global cList
		#helper.printList(cList)
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
		print "TEST test_simple end___________________________"
	def test_uniqueAdvertizer(self):
		pass

	def test_distribution100(self):
		print "TEST test_distribution100 init___________________________"
		creatives = helper.buildRandom(300)
		print "test 3 creatives list!"
		#helper.printList(creatives)
		a = auction.Auction()
		dict = {}
		winners = set()
		for i in range(0, 10):
			#print "iteration: " + str(i)
			res = a.perform(creatives, 6, "AS")
			print "res #" + str(i)
			print res
			print "--------------------------------------------------"
			for c in res: 
				#dict [str(c)] += 1
				if str(c.ID)+"adv"+str(c.advertizer_id) in winners:
					dict[str(c.ID)+"adv"+str(c.advertizer_id)] += 1
				else:
					winners.add(str(c.ID)+"adv"+str(c.advertizer_id))
					dict[str(c.ID)+"adv"+str(c.advertizer_id)] = 0
			#print dict
		print "__________________________________DICTS_____________________________________"
		print dict
		print "TEST test_distribution100 end___________________________"

if __name__ == '__main__':
	prepareCreatives()
	unittest.main()