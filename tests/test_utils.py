import unittest
from utils.utils import Utils

class VerifyUtils(unittest.TestCase):
    def find_numeric_values(self):
        text_one = "dsfknn1421429vgfdsvcxv"
        response_one = Utils.find_speed(text_one)

        text_two = "ilovepython"
        response_two = Utils.find_speed(text_two)

        self.assertEqual(1421429, response_one)
        self.assertEqual(0, response_two)
        
