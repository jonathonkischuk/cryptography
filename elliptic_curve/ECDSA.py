# ELLIPTIC CURVE DIGITAL SIGNATURE ALGORITHM
from Crypto.Hash import SHA256
# ECC elliptic curve cryptography
from Crypto.PublicKey import ECC
# DSS digital signature standard
from Crypto.Signature import DSS


key = ECC.generate(curve='P-256')

# print(key)
# print(key.public_key())

message = "Transaction #29102932 in the amount of 3.72 BTC delivered from wallet 90292333 to wallet 220872635"
# any messages are converted to 256 bits long hash
message_hash = SHA256.new(message.encode('utf-8'))

signer = DSS.new(key, "fips-186-3")
signature = signer.sign(message_hash)

print(signature)

# verify the signature
verifier = DSS.new(key, "fips-186-3")

try:
    verifier.verify(message_hash, signature)
    print("Signature verified")
except ValueError:
    print("Signature verification failed")
