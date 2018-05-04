import unittest
from d3_e5_fibonacci import fibonacci_maker

class TestFibonacciFunc(unittest.TestCase): 
    
    def test_if_fibo_bigger2(self):
        self.assertEqual(fibonacci_maker(4), 3)

    def test_if_fibo_smaller2(self):
        self.assertEqual(fibonacci_maker(1), 1)

if __name__ == '__main__':
    unittest.main()