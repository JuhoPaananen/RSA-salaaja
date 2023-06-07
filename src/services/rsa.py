def encrypt(message: str, public_key: tuple) -> int:
    """Function for encrypting a message using RSA

    Args:
        message (str): Plaintext message
        public_key (tuple): public key in the form (e, N) tuple

    Returns:
        int: Encrypted message as an integer
    """
    message_bytes = message.encode("utf-8")
    message_int = int.from_bytes(message_bytes, "big")
    public_e, modulus = public_key
    encrypted_msg = pow(message_int, public_e, modulus)
    return encrypted_msg

def decrypt(encrypted_msg: int, private_key: tuple) -> str:
    """Function for decrypting a message using RSA

    Args:
        encrypted_msg (int): Encrypted message in the form of a an integer
        private_key (tuple): private key in the form (d, N) tuple

    Returns:
        str: Decrypted message
    """
    private_d, modulus = private_key
    decrypted_msg_int = pow(encrypted_msg, private_d, modulus)
    # Find out the length of the original message in bytes,
    # add 7 so that // 8 rounds up to the nearest whole byte
    # Message length can not exceed the length of the modulus N,
    # so it can contain N // 8 bytes, default 256 bytes
    bytes_in_message = (decrypted_msg_int.bit_length() + 7) // 8
    # to_bytes requires the length of the byte array to be specified
    bytes_message = decrypted_msg_int.to_bytes(bytes_in_message, "big")
    message = bytes_message.decode("utf-8", errors="ignore")
    return message
