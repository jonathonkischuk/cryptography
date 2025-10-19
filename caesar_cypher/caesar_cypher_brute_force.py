ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def caesar_encrypt(plain_text):
    KEY = len(plain_text) % len(ALPHABET)
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


def crack_caesar_cypher(cipher_text):
    for key in range(len(ALPHABET)):
        plain_text = ''

        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plain_text += ALPHABET[index]

        print('With key %s, the result is %s' % (key, plain_text))


if __name__ == '__main__':
    encrypted = caesar_encrypt('This is a new test text message')
    crack_caesar_cypher(encrypted)
