import unittest
from d3_e3_anagram import Anagram

class TestAnagram(unittest.TestCase): 
    
    def test_is_not_anagram(self): #not an anagram
        anagram = Anagram()
        self.assertEqual(anagram.is_anagram('anna', 'annn'), False)

    def test_is_anagram(self): #not an anagram
        anagram = Anagram()
        self.assertEqual(anagram.is_anagram('anna', 'anna'), True)

    # def test_if_string(): #?
    #     pass

    # def test_if_string_sorted(): #?
    #     pass

if __name__ == '__main__':
    unittest.main()