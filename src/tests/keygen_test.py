import unittest
from services.keygen import KeyGenerator
from utils import eratosthene_sieve

class TestKeyGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.keygen = KeyGenerator()
        self.filter_primes = eratosthene_sieve(10000)
        self.non_primes = [i for i in range(3,10000, 2) if i not in self.filter_primes]

    def test_generate_prime(self):
        self.keygen.key_length = 13
        self.assertTrue(self.keygen.generate_prime() in self.filter_primes)