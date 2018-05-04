import unittest
import d3_e6_extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_3_is_5(self):
        self.assertEqual(d3_e6_extend.add(2, 3), 5)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(d3_e6_extend.add(4, 1), 5)

    def test_max_of_three_first(self):
        self.assertEqual(d3_e6_extend.max_of_three(5, 4, 3), 5)

    def test_max_of_three_third(self):
        self.assertEqual(d3_e6_extend.max_of_three(3, 4, 5), 5)

    def test_median_four(self):
        self.assertEqual(d3_e6_extend.median([7,5,3,5]), 5)

    def test_median_five(self):
        self.assertEqual(d3_e6_extend.median([1,2,3,4,5]), 3)

    def test_is_vowel_a(self):
        self.assertFalse(d3_e6_extend.is_vowel('t'))

    def test_is_vowel_u(self):
        self.assertTrue(d3_e6_extend.is_vowel('e'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(d3_e6_extend.translate('alma'), 'avalmava')

    def test_translate_kolbice(self):
        self.assertEqual(d3_e6_extend.translate('kolbice'), 'kovolbiviceve')

if __name__ == '__main__':
    unittest.main()