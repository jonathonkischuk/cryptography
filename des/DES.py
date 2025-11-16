from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

key = b"mysecret"
plain_text = b'This is the plaintext'

def des_encrypt(plaintext, key):
    cipher_text = DES.new(key, DES.MODE_CBC)
    iv = cipher_text.iv
    cipher_text = cipher_text.encrypt(pad(plaintext, DES.block_size))
    return iv, cipher_text


iv, cipher = des_encrypt(plain_text, key)
print(binascii.hexlify(cipher))


def des_decrypt(cipher, key, iv):
    decrypt_cipher = DES.new(key, DES.MODE_CBC, iv)
    original = decrypt_cipher.decrypt(cipher)
    original = unpad(original, DES.block_size)
    return original


original_text = des_decrypt(cipher, key, iv)
print(original_text.decode())
