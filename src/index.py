from services.keygen import generate_keys
from services.rsa import encrypt, decrypt


def main():
    """Main method.
    """
    keys = generate_keys()

    test_message = input("Enter a message to encrypt: ")
    print(f"Test message: {test_message}")

    cipher_text = encrypt(test_message, keys[0])
    print(f"Encrypted: {cipher_text}")

    plain_text = decrypt(cipher_text, keys[1])
    print(f"Decrypted: {plain_text}")

if __name__ == "__main__":
    main()
