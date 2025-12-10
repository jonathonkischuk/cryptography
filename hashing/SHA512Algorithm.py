from hashlib import sha512


# output is a 512 bits long sequence (message digest)
# this is the hash Bitcoin uses
# result is a 128 character long hexadecimal sequence
s1 = "Hello, this is a SHA256 message sequence example"
s2 = "Hello, this is a SHA256 message sequence example"


result1 = sha512(s1.encode())
print(result1.hexdigest())
result2 = sha512(s2.encode())
print(result2.hexdigest())
