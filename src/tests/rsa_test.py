import unittest
from services.keygen import KeyGenerator
from services.rsa import Cipher

class TestCipher(unittest.TestCase):
    def setUp(self) -> None:
        self.cipher = Cipher()
        self.public_key, self.private_key = KeyGenerator().generate_keys()
        self.message = "Hello, this text will be encrypted and decrypted!"

    def test_encryption(self):
        cipher_text = self.cipher.encrypt(self.message, self.public_key)
        self.assertTrue(cipher_text != self.message)

    def test_encryption_length(self):
        cipher_text = self.cipher.encrypt(self.message, self.public_key)
        bit_length = cipher_text.bit_length()
        self.assertTrue(bit_length <= 2048)

    def test_decryption(self):
        cipher_text = self.cipher.encrypt(self.message, self.public_key)
        plain_text = self.cipher.decrypt(cipher_text, self.private_key)
        self.assertTrue(self.message == plain_text)

