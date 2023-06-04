from utils import (
    generate_prime,
    find_e
)

# Handbook of Applied Cryptography (chapter 4) states that 3 trials is sufficient for
# 1024 bit numbers. However, many discussions online recommend 40 trials for probability
# of 2^-80 for a non-prime to pass the test

def generate_keys() -> tuple:
    """
    Method that generates a public and private key pair. This follows the steps outlined on
    Wikipedia - RSA: https://fi.wikipedia.org/wiki/RSA

    Returns:
        tuple: A tuple containing the public and private key pair.
    """
    first_prime = generate_prime()
    second_prime = generate_prime()
    while first_prime == second_prime:
        second_prime = generate_prime()

    modulus = first_prime * second_prime

    # phi(N), where N = p * q and p, q are primes
    phi = (first_prime - 1) * (second_prime - 1)

    # 1 < e < N, such that e = 1 mod phi
    public_e = find_e(modulus, phi)

    # Choose d so that d*e = 1 mod phi --> d = e^-1 mod phi
    private_d = pow(public_e, -1, phi)

    public_key = (public_e, modulus)
    private_key = (private_d, modulus)
    del first_prime, second_prime, modulus, phi, public_e, private_d

    return public_key, private_key
