import unittest
import blackjack

class BlackjackTest(unittest.TestCase):
	# This is where you're tests can go!
	# Each test must take "self" as an arguement.
	
# 	def test_is_bust_1(self):
# 	    bust_result = blackjack.is_bust(["J"])
# 	    self.assertEqual(bust_result,False)

# 	def test_is_bust_2(self):
# 	    bust_result = blackjack.is_bust(["20"])
# 	    self.assertEqual(bust_result,False)
	    
# 	def test_is_bust_3(self):
# 	    bust_result = blackjack.is_bust(["4","Q","J","10"])
# 	    self.assertEqual(bust_result,True)
	    
# 	def test_get_card_value_1(self):
# 	    value = blackjack.get_card_value(["2"])
# 	    self.assertEqual(value,2)

# 	def test_get_card_value_2(self):
# 	    value = blackjack.get_card_value(["2","J","Q"])
# 	    self.assertEqual(value,22)
	    
# 	def test_get_card_value_3(self):
# 	    value = blackjack.get_card_value(["3","9"])
# 	    self.assertEqual(value,12)
	    
	def test_is_bust_1(self):
	    bust_result = blackjack.is_bust(["J"])
	    self.assertEqual(bust_result,False)

	def test_is_bust_2(self):
	    bust_result = blackjack.is_bust(["20"])
	    self.assertEqual(bust_result,False)
	    
	def test_is_bust_3(self):
	    bust_result = blackjack.is_bust(["4","Q","J","10"])
	    self.assertEqual(bust_result,True)
	    
	def test_get_card_value_1(self):
	    value = blackjack.get_card_value(["2"])
	    self.assertEqual(value,2)

	def test_get_card_value_2(self):
	    value = blackjack.get_card_value(["2","J","Q"])
	    self.assertEqual(value,22)
	    
	def test_get_card_value_3(self):
	    value = blackjack.get_card_value(["3","9"])
	    self.assertEqual(value,12)
# 	# Write three more tests!

# Don't touch anything under this.
if __name__ == '__main__':
    unittest.main()