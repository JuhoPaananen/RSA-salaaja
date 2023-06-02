from services.keygen import KeyGenerator
from services.rsa import Cipher


def main():
    """Main method.
    """
    keygen = KeyGenerator()
    cipher = Cipher()
    keys = keygen.generate_keys()
    
    test_message = input("Enter a message to encrypt: ")
    print(f"Test message: {test_message}")
    
    cipher_text = cipher.encrypt(test_message, keys[0])
    print(f"Encrypted: {cipher_text}")

    plain_text = cipher.decrypt(cipher_text, keys[1])
    print(f"Decrypted: {plain_text}")

if __name__ == "__main__":
    main()
