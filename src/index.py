from services.keygen import KeyGenerator


def main():
    """Main method.
    """
    keygen = KeyGenerator()
    prime = keygen.generate_prime()
    print(prime)

if __name__ == "__main__":
    main()
