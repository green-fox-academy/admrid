import unittest
from d3_e4_count_letters import string_to_dict

class TestDict(unittest.TestCase): 
    
    def test_string_to_dict(self):
        self.assertEqual(string_to_dict('anna'), {"a":2, "n":2})

if __name__ == '__main__':
    unittest.main()