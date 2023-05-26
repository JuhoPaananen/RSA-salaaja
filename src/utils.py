import random

"""
Module that contains utility functions for the project.
"""
def eratosthene_sieve(n: int) -> list:
    """
    Method that generates a list of prime numbers using the Sieve of Eratosthene.
    This will be used to speed up the Rab-Miller test.

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

def miller_rabin_test(n:int, k:int) -> bool:
    """
    Method that checks if a candidate odd number is prime using the Miller-Rabin test.
    This implementation is based on the pseudocode from the Wikipedia article:
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

    Args:
        n (int): An odd prime candidate
        k (int): Number of trials

    Returns:
        bool: Returns True if the candidate is likely prime, otherwise returns False.
    """

    s = 0
    d = n - 1
    while d % 2 == 0:
        d = d // 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n) # a more efficient function for x = a**d % n

        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y

        if y != 1:
            return False

    return True