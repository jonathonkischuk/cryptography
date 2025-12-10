from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

from des.DES import plain_text

# RSA (Public key and private key)
# RSA encrypts a session key (AES)
# RSA is slow bc it uses extremely large numbers

# generate the keys
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# print(private_key.exportKey())
# print(public_key.exportKey())

# file = open('mykey.pem', 'wb')
# file.write(key.exportKey())

### RSA ENCRYPTION ###
# the utf8 passed to encode() is technically not needed as it is the default value
data = "This is just a simple test message".encode("utf8")

# this is the private key in AES (16 bytes for the private key)
# used by sender as well as receiver
session_key = get_random_bytes(16)
print("Session key:", session_key)

# encrypt session key with public RSA key
# encryption --- public key
encrypt_rsa = PKCS1_OAEP.new(public_key)

# encrypted version of session key
# send to receiver
enc_session_key = encrypt_rsa.encrypt(session_key)
print("Encrypted session key:", enc_session_key)

# encrypt data with AES encrypted session key
cipher_aes = AES.new(session_key, AES.MODE_GCM)
nonce = cipher_aes.nonce

# digest can be used for auth
cipher_text, tag = cipher_aes.encrypt_and_digest(data)
print("Cipher text:", cipher_text)
print("Tag:", tag)


### RSA DECRYPTION ###
# receiver must have: RSA private key, tag, nonce
decrypt_rsa = PKCS1_OAEP.new(private_key)
sess_key = decrypt_rsa.decrypt(enc_session_key)
print("Decrypted session key:", sess_key)

decrypt_aes = AES.new(sess_key, AES.MODE_GCM, nonce)
plaintext = decrypt_aes.decrypt_and_verify(cipher_text, tag)
print("Plain text:", plaintext.decode("utf8"))
