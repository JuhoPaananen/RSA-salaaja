import unittest
from services.keygen import generate_keys
from services.rsa import encrypt, decrypt

class TestCipher(unittest.TestCase):
    def setUp(self) -> None:
        self.public_key, self.private_key = generate_keys()
        self.message = "Hello, this text will be encrypted and decrypted!"

    def test_encryption(self):
        cipher_text = encrypt(self.message, self.public_key)
        self.assertTrue(cipher_text != self.message)

    def test_encryption_length(self):
        cipher_text = encrypt(self.message, self.public_key)
        bit_length = cipher_text.bit_length()
        self.assertTrue(bit_length <= 2048)

    def test_decryption(self):
        cipher_text = encrypt(self.message, self.public_key)
        plain_text = decrypt(cipher_text, self.private_key)
        self.assertTrue(self.message == plain_text)

