import unittest
from d3_e2_summer import SummEr

class TestList(unittest.TestCase):
    def test_empyt_list(self):
        thesummer = SummEr()
        self.assertEqual(thesummer.summer([]), 0)

    def test_list_oneitem(self):
        thesummer = SummEr()
        self.assertEqual(thesummer.summer([1]), 1)

    def test_list_multiitem(self):
        thesummer = SummEr()
        self.assertEqual(thesummer.summer([1, 2, 3]), 6)

    def test_list_null(self):
        thesummer = SummEr()
        self.assertEqual(thesummer.summer([0]), 0)


if __name__ == '__main__':
    unittest.main()