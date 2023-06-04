import random


def eratosthene_sieve(max_number: int) -> list:
    """
    Method that generates a list of prime numbers using the Sieve of Eratosthene.
    This will be used to speed up the Rab-Miller test.

    Args:
        max_number (int): The number up to which the list of primes will be generated.

    Returns:
        list: A list of primes up to n.
    """
    primes = [True] * (max_number + 1)
    primes[0] = False
    primes[1] = False
    for i in range(int(max_number**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_number + 1, i):
                primes[j] = False
    return [i for i in range(max_number) if primes[i]]

def miller_rabin_test(candidate:int, trials:int = 40) -> bool:
    """
    Method that checks if a candidate odd number is prime using the Miller-Rabin test.
    This implementation is based on the pseudocode from the Wikipedia article:
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

    Args:
        candidate (int): An odd prime candidate
        trials (int): Number of trials. Defaults to 40.

    Returns:
        bool: Returns True if the candidate is likely prime, otherwise returns False.
    """

    power = 0
    odd_multiplier = candidate - 1
    while odd_multiplier % 2 == 0:
        odd_multiplier = odd_multiplier // 2
        power += 1

    for _ in range(trials):
        random_int = random.randint(2, candidate - 1)
        test_value = pow(random_int, odd_multiplier, candidate)

        for _ in range(power):
            new_test_value = pow(test_value, 2, candidate)
            if new_test_value == 1 and test_value != 1 and test_value != candidate - 1:
                return False
            test_value = new_test_value

        if new_test_value != 1:
            return False

    return True

def euclidean_algorithm(first_number: int, second_number: int) -> int:
    """
    Method that returns the greatest common divisor of two numbers.

    Args:
        first_number (int): First number
        second_number (int): Second number

    Returns:
        int: The greatest common divisor of first and second number
    """
    remainder = first_number % second_number
    while remainder != 0:
        first_number = second_number
        second_number = remainder
        remainder = first_number % second_number
    return second_number

def generate_prime(bits: int = 1024) -> int:
    """
    Method that generates a prime number of given length in bits.
    Method utilizes the Eratosthene sieve and the Miller-Rabin test.

    Args:
        bits (int): The length of the prime number in bits. Defaults to 1024 bits.

    Returns:
        int: Returns a likely prime number of length n bits.
    """
    filter_primes = eratosthene_sieve(1000)
    while True:
        candidate = random.randrange(2**(bits-1) + 1, 2**bits-1)
        if all(candidate % prime != 0 for prime in filter_primes):
            if miller_rabin_test(candidate):
                return candidate

def find_e(modulus: int, phi: int) -> int:
    """
    Method that finds a suitable e for the RSA algorithm. e must be coprime with phi(N).

    Args:
        n (int): The product of two primes p and q.
        phi (int): phi(N) = (p - 1)(q - 1).

    Returns:
        int: A suitable e for the RSA algorithm.
    """
    while True:
        candidate_e = random.randrange(2, modulus)
        if euclidean_algorithm(candidate_e, phi) == 1:
            return candidate_e
