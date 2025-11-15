ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ENGLISH_WORDS = []

def get_data():
    dictionary = open('english_words.txt', 'r')

    for word in dictionary.read().split('\n'):
        ENGLISH_WORDS.append(word)

    dictionary.close()
    # print(len(ENGLISH_WORDS))


def count_words(text):
    text = text.upper()
    words = text.split(' ')
    matches = 0

    for word in words:
        if word in ENGLISH_WORDS:
            matches += 1

    return matches


def is_text_english(text):
    matches = count_words(text)
    if (float(matches) / len(text.split(' '))) * 100 >= 65:
        return True
    return False


def caesar_crack(cipher_text):
    for key in range(len(ALPHABET)):
        plain_text = ''

        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plain_text += ALPHABET[index]

        if is_text_english(plain_text):
            print("We have managed to crack Caesar cipher, the key is: %s, the message is %s" % (key, plain_text))


if __name__ == '__main__':
    get_data()
    # plain_text = "My name is Carlos DeBarlos from Tazmania. I am a penguin who loves to sneak around, getting into all sorts of trouble. I may get into precarious situations, but deep down I am the kindest penguin you will find. If you are ever in Tazmania, or if I meet you on my travels around the world, we are sure to have a great time. Keep an eye on me though, because trouble finds me everywhere!"
    # print(is_text_english(plain_text))

    encrypted = 'WKLVCLVCDCWHVWCKHOSCPHCILQGCPACZDACKRPHCDQGCJHWCLQCEXWCLWBVCORFNHGCZKDWCFRXOGCWKHCNHACEH'
    caesar_crack(encrypted)
