import unittest
import random
import math
from utils import eratosthene_sieve, miller_rabin_test, euclidean_algorithm, generate_prime, find_e

class TestPrimeNumberTools(unittest.TestCase):
    def setUp(self):
        self.filter_primes = eratosthene_sieve(10000)
        self.non_primes = [i for i in range(3,10000, 2) if i not in self.filter_primes]

    def test_eratosthene_sieve(self):
        self.assertEqual(eratosthene_sieve(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    def test_miller_rabin_for_known_primes(self):
        for prime in self.filter_primes[2:]:
            self.assertTrue(miller_rabin_test(prime, 40))

    def test_miller_rabin_for_non_primes(self):
        for non_prime in self.non_primes:
            self.assertFalse(miller_rabin_test(non_prime, 40))

    def test_generate_prime(self):
        self.assertTrue(generate_prime(13) in self.filter_primes)

    def test_euclidean_algorithm_finds_gcd(self):
        self.assertEqual(euclidean_algorithm(12, 5), 1)
        self.assertEqual(euclidean_algorithm(7, 12), 1)
        self.assertEqual(euclidean_algorithm(12, 8), 4)
        self.assertEqual(euclidean_algorithm(4, 12), 4)
        self.assertEqual(euclidean_algorithm(12, 9), 3)
        self.assertEqual(euclidean_algorithm(9, 12), 3)

    def test_find_e_generates_correct_number(self):
        p = random.choice(self.filter_primes)
        q = random.choice(self.filter_primes)
        while p == q:
            q = random.choice(self.filter_primes)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = find_e(n, phi)
        self.assertEqual(math.gcd(e, phi), 1)

    
