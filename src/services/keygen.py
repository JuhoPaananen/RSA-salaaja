KEY_LENGTH = 2**1024

class KeyGenerator:
    """Class that handles the generation of keys for the RSA algorithm.
    """

    def __init__(self):
        """Constructor method.
        """
        self.key_length = KEY_LENGTH

    def eratosthene_sieve(self, n: int) -> list:
        """Method that generates a list of prime numbers using the Sieve of Eratosthene. This will be used to speed up the Rab-Miller test.

        Args:
            n (int): The number up to which the list of primes will be generated.

        Returns:
            list: A list of primes up to n.
        """
        primes = [True] * (n + 1)
        primes[0] = False 
        primes[1] = False
        for i in range(int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(n) if primes[i]]

    def miller_rabin_test(self, n:int, k:int) -> bool:
        return False


primes = KeyGenerator().eratosthene_sieve(1000)
print(primes)
