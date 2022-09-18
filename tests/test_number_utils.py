from src.__init__ import is_even_number
import unittest

class EvenNumbersTest(unittest.TestCase):
    def test_give_2_return_even_number(self):
        num = 2 
        test = is_even_number(num)
        self.assertEqual(test, 'even number', 'Fail')
        
    def test_give_0_return_even_number(self):
        num = 0
        test = is_even_number(num)
        self.assertEqual(test, 'even number', 'Fail')
        
class  OddNumbersTest(unittest.TestCase):
    def test_give_1_return_odd_number(self):
        num = 1
        test = is_even_number(num)
        self.assertEqual(test, 'odd number', 'Fail')
        
    def test_give_3_return_odd_number(self):
        num = 3
        test = is_even_number(num)
        self.assertEqual(test, 'odd number', 'Fail')