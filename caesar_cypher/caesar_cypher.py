# we use alphabet bc we convert letters to numbers
# so we can use mathematical operations
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3


def caesar_encrypt(plain_text):
    # the encrypted message
    cipher_text = ''
    # make the algorithm case-insensitive
    plain_text = plain_text.upper()

    # consider all plain_text letters
    for c in plain_text:
        # find numerical representation (index) associated
        # with that character in the alphabet
        index = ALPHABET.find(c)
        # this encryption is a character shift based on the key
        # use modular arithmetic to transform values in the range
        # range is [0, num_of_letters_in_alphabet]
        index = (index + KEY) % len(ALPHABET)
        # keep appending encrypted char to cipher text
        cipher_text = cipher_text + ALPHABET[index]

    return cipher_text


def caesar_decrypt(cipher_text):
    plain_text = ''

    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index - KEY) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]

    return plain_text


if __name__ == '__main__':
    m = "Welcome to the Udemy Course"
    encrypted = caesar_encrypt(m)
    print(encrypted)

    decrypted = caesar_decrypt(encrypted)
    print(decrypted)
