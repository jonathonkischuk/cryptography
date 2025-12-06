import random
from math import floor, sqrt

RANDOM_START = int(1e3)
RANDOM_END = int(1e5)


def isPrime(num):
    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, floor(sqrt(num))):
        if num % i == 0:
            return False

    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def modular_inverse(a, b):
    if a == 0:
        return b, 0, 1

    div, x1, y1 = modular_inverse(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return div, x, y


def generate_large_prime(start=RANDOM_START, end=RANDOM_END):
    num = random.randint(start, end)

    while not isPrime(num):
        num = random.randint(start, end)

    return num


def generate_rsa_keys():
    p = generate_large_prime()
    q = generate_large_prime()

    n = p * q

    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)

    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = modular_inverse(e, phi)[1]

    return (d, n), (e, n)


def encrypt(public_key, plain_text):
    e, n = public_key

    cipher_text = []
    # consider characters one by one and use modular exponentiation
    for char in plain_text:
        a = ord(char)
        cipher_text.append(pow(a, e, n))

    return cipher_text


def decrypt(private_key, cipher_text):
    d, n = private_key

    plain_text = ""
    for num in cipher_text:
        a = pow(num, d, n)
        plain_text = plain_text + str(chr(a))

    return plain_text


if __name__ == "__main__":
    private_key, public_key = generate_rsa_keys()

    message = "This is a test message with an RSA algorithm."
    print("Original message: %s" % message)
    cipher_text = encrypt(public_key, message)
    print("Cipher text: %s" % cipher_text)
    plain_text = decrypt(private_key, cipher_text)
    print("Decrypted text: %s" % plain_text)
