from services.keygen import KeyGenerator


def main():
    """Main method.
    """
    keygen = KeyGenerator()
    primes = keygen.eratosthene_sieve(1000)
    print(primes)

if __name__ == "__main__":
    main()

