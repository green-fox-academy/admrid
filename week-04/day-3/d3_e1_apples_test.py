import unittest
from d3_e1_apples import Apple

class TestString(unittest.TestCase):
    def test_string(self):
        apple = Apple()
        self.assertEqual(apple.get_apple(), 'apple')

if __name__ == '__main__':
    unittest.main()