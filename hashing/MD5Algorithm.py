# message digest 5
from hashlib import md5


s = "This is a test message"

result = md5(s.encode())
# 32 hexadecimal characters
# nibbles (we can store a hexadecimal character on 4 bits or 0.5 bytes)
print(result.hexdigest())