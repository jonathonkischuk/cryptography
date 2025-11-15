# in production, we would use secrets rather than random
from random import randint

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ.,-"


def encrypt(text, key):
    text = text.upper()
    cipher_text = ''

    for index, char in enumerate(text):
        key_index = key[index]

        char_index = ALPHABET.find(char)
        cipher_text += ALPHABET[(char_index + key_index) % len(ALPHABET)]

    return cipher_text


def decrypt(cipher, key):
    plain = ''

    for index, char in enumerate(cipher):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        plain += ALPHABET[(char_index - key_index) % len(ALPHABET)]

    return plain


def random_sequence(text):
    random = []

    for _ in range(len(text)):
        random.append(randint(0, len(ALPHABET) - 1))

    return random


if __name__ == '__main__':
    message = "Execution of a program requires an implementation. There are two main approaches for implementing a programming language – compilation, where programs are compiled ahead-of-time to machine code, and interpretation, where programs are directly executed. In addition to these two extremes, some implementations use hybrid approaches such as just-in-time compilation and bytecode interpreters."
    seq = random_sequence(message)
    print("Original message:", message)
    cipher_text = encrypt(message, seq)
    print("Encrypted message:", cipher_text)
    decrypted_text = decrypt(cipher_text, seq)
    print("Decrypted message:", decrypted_text)
