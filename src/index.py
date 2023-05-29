from services.keygen import KeyGenerator


def main():
    """Main method.
    """
    keygen = KeyGenerator()
    keys = keygen.generate_keys()
    public_key = keys[0][1]
    print(public_key)

if __name__ == "__main__":
    main()
