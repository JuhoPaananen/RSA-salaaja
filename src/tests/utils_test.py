import unittest
import random
import math
import rsa
from utils import _eratosthene_sieve, _miller_rabin_test, _euclidean_algorithm, generate_prime, find_e

class TestPrimeNumberTools(unittest.TestCase):
    def setUp(self):
        self.filter_primes = _eratosthene_sieve(10000)
        self.non_primes = [i for i in range(3,10000, 2) if i not in self.filter_primes]
        self.large_primes = [2**607-1, 2**521-1, 2**1279-1] # source: https://en.wikipedia.org/wiki/Largest_known_prime_number
        # Using RSA library to generate 2048 bit non-prime numbers as N in keys is a product of two primes p*q
        self.non_prime_n = []
        for _ in range(10):
            self.non_prime_n.append(rsa.newkeys(2048)[0].n)
            self.non_prime_n.append(self.large_primes[0] * self.large_primes[1])

    def test_eratosthene_sieve(self):
        self.assertEqual(_eratosthene_sieve(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    def test_miller_rabin_for_known_small_primes(self):
        for prime in self.filter_primes[2:]:
            self.assertTrue(_miller_rabin_test(prime, 40))

    def test_miller_rabin_for_small_non_primes(self):
        for non_prime in self.non_primes:
            self.assertFalse(_miller_rabin_test(non_prime, 40))

    def test_miller_rabin_for_large_primes(self):
        for prime in self.large_primes:
            self.assertTrue(_miller_rabin_test(prime, 40))

    def test_miller_rabin_for_product_of_large_primes(self):
        candidate = self.large_primes[0] * self.large_primes[1]
        self.assertFalse(_miller_rabin_test(candidate, 40))

    def test_miller_rabin_2048_bit_non_prime(self):
        for non_prime in self.non_prime_n:
            self.assertFalse(_miller_rabin_test(non_prime, 40))

    def test_generate_prime_generates_prime(self):
        self.assertTrue(generate_prime(13) in self.filter_primes)

    def test_euclidean_algorithm_finds_gcd(self):
        for _ in range(10):
            first_number = random.randint(1, 100000000)
            second_number = random.randint(1, 100000000)
            self.assertEqual(_euclidean_algorithm(first_number, second_number), math.gcd(first_number, second_number))

    def test_find_e_generates_correct_number(self):
        p = random.choice(self.filter_primes)
        q = random.choice(self.filter_primes)
        while p == q:
            q = random.choice(self.filter_primes)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = find_e(n, phi)
        self.assertEqual(math.gcd(e, phi), 1)

    
