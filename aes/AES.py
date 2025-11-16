from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib


# 128 bits (16 bytes)
# key = get_random_bytes(16)

# if using a user password, it must be 16 bytes (aka 16 characters at 1 byte per char)
# ask for a password - and then use a SHA (hashing) 16 bytes (this ensures 16 bytes)
# key = b'mysecretpassword'
# plaintext = b'This is a message, slated for AES encryption testing.'


def get_key_from_password(password: str) -> bytes:
    pass_bytes = password.encode('utf-8')
    full_hash = hashlib.sha256(pass_bytes).digest()
    return full_hash[:16] # AES-128 Key


def aes_encrypt(plain_text, _key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plain_text, AES.block_size))
    iv = cipher.iv
    return iv, ciphertext


def aes_decrypt(cipher_text, _key, iv):
    decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
    original = unpad(decrypt_cipher.decrypt(cipher_text), AES.block_size)
    return original.decode('utf-8')


user_password = input("Enter your passkey: \n")
key = get_key_from_password(user_password)

user_plaintext = input("\nEnter your plaintext: \n")
plaintext_bytes = user_plaintext.encode('utf-8')

iv, cipher_text = aes_encrypt(plaintext_bytes, key)
original_text = aes_decrypt(cipher_text, key, iv)

print('\n', cipher_text)
print('\n', original_text)
