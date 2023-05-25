import unittest
from services.keygen import KeyGenerator

class TestKeyGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.keygen = KeyGenerator()
        #return super().setUp()
    
    def test_eratosthene_sieve(self):
        self.assertEqual(self.keygen.eratosthene_sieve(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])