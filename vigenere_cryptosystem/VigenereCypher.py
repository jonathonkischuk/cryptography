ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()

    cipher_text = ''
    key_index = 0

    for character in plain_text:
        index = (ALPHABET.find(character) + ALPHABET.find(key[key_index])) % len(ALPHABET)

        cipher_text += ALPHABET[index]
        key_index += 1

        if key_index == len(key):
            key_index = 0

    return cipher_text


def vigener_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()

    plain_text = ''
    key_index = 0
    for character in cipher_text:
        index = (ALPHABET.find(character) - ALPHABET.find(key[key_index])) % len(ALPHABET)
        plain_text += ALPHABET[index]

        key_index += 1
        if key_index == len(key):
            key_index = 0

    return plain_text


if __name__ == '__main__':
    text = "Cryptography is quite important in cryptocurrencies"
    cipher = vigenere_encrypt(text, 'Animal')
    print(vigener_decrypt(cipher, 'Animal'))