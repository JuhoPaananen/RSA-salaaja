from utils import (
    generate_prime,
    find_e
)

# Handbook of Applied Cryptography (chapter 4) states that 3 trials is sufficient for
# 1024 bit numbers. However, many discussions online recommend 40 trials for probability
# of 2^-80 for a non-prime to pass the test

class KeyGenerator:
    """
    Class that handles the generation of keys for the RSA algorithm.
    """

    def generate_keys(self) -> tuple:
        """
        Method that generates a public and private key pair. This follows the steps outlined on 
        Wikipedia - RSA: https://fi.wikipedia.org/wiki/RSA

        Returns:
            tuple: A tuple containing the public and private key pair.
        """
        p = generate_prime()
        q = generate_prime()
        while p == q:
            q = generate_prime()
        
        N = p * q
        
        # phi(N), where N = p * q and p, q are primes
        phi = (p - 1) * (q - 1)
        
        # 1 < e < N, such that e = 1 mod phi
        e = find_e(N, phi)
        
        # Choose d so that d*e = 1 mod phi --> d = e^-1 mod phi
        d = pow(e, -1, phi)
        
        public_key = (e, N)
        private_key = (d, N)
        del p, q, N, phi, e, d
        
        return public_key, private_key
        
       