import random
#from utils import eratosthene_sieve, miller_rabin_test
from utils import eratosthene_sieve, miller_rabin_test

KEY_LENGTH = 1024 # bits
NUMBER_OF_TRIALS = 40
# Handbook of Applied Cryptography (chapter 4) states that 3 trials is sufficient for
# 1024 bit numbers. However, many discussions online recommend 40 trials for probability
# of 2^-80 for a non-prime to pass the test

class KeyGenerator:
    """
    Class that handles the generation of keys for the RSA algorithm.
    """

    def __init__(self):
        self.key_length = KEY_LENGTH
        self.filter_primes = eratosthene_sieve(1000)

    def generate_prime(self) -> int:
        """
        Method that generates a prime number of length KEY_LENGTH bits.

        Returns:
            int: Returns a likely prime number of length KEY_LENGTH bits.
        """
        while True:
            candidate = random.randrange(2**(self.key_length-1) + 1, 2**(self.key_length)-1)
            if all(candidate % prime != 0 for prime in self.filter_primes):
                if miller_rabin_test(candidate, NUMBER_OF_TRIALS):
                    return candidate
