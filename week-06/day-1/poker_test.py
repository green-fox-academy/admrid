import unittest
from poker import Poker

class Poker_test(unittest.TestCase):

   def test_poker(self):
       p = Poker()
       self.assertEqual(p.check_hands('Black: 2H 3D 5S 9C KD', 'White: 2C 3H 4S 8C AH'), 'White wins! - (High card: Ace)')

   def test_poker_again(self):
       p = Poker()
       self.assertEqual(p.check_hands('Black: 2H 4S 4C 2D 4H', 'White: 2S 8S AS QS 3S'), 'White wins! - (Flush: A)')

if __name__ == '__main__':
   unittest.main()