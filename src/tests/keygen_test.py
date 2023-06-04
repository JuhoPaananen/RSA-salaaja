import unittest
from unittest.mock import Mock, patch
from services.keygen import generate_keys
from utils import eratosthene_sieve

class TestKeyGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.public_key, self.private_key = generate_keys()

    def test_key_values(self):
        self.assertTrue(self.public_key[1] == self.private_key[1])
        self.assertTrue(self.public_key[0] != self.private_key[0])
        self.assertTrue(self.private_key[1] > 0)

    def test_key_length_for_modulus(self):
        self.assertTrue(self.public_key[1].bit_length() == 2048)
