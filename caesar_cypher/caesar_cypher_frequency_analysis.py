import matplotlib.pylab as plt


LETTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def frequency_analysis(text):
    text = text.upper()

    letter_frequencies = {}

    for letter in LETTERS:
        letter_frequencies[letter] = 0

    for letter in text:
        if letter in LETTERS:
            letter_frequencies[letter] += 1

    return letter_frequencies


def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()


def caesar_crack(cipher_text):
    freq = frequency_analysis(cipher_text)
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print("The possible key value: %s" % (LETTERS.find(freq[0][0]) -
                                          LETTERS.find('E')))


if __name__ == '__main__':
    cipher_text = "VKDQQRQCGHILQHGCWKHCTXDOLWACRICLQIRUPDWLRQCSURGXFHGCEACDCVRXUFHCIRUCH DPSOHBCWKHCTXDOLWACLQCDCPHVVDJHCEACDCIRUPXODCVLPLODUCWRCWKHCHTXDWLRQCWKDWCGHILQHVCWKHUPRGAQDPLFCHQWURSACLQCSKAVLFVBCLQCLWVCPRVWCEDVLFCWHUPVBCLWCFDQCEHCIRXQGCWKDWCGHYHORSPHQWCDQGCSURJUDPPLQJCFDQCKHOSCDGYDQFHCWKHCVXEMHFWCPDWWHUCDQGCLWVCSHUIRUPDQFHBCZKLOHCFODVVLFCELWVCFDQCEHCYHUACSRZHUIXOBCTXDQWXPCELWVBCRUCTXELWVBCFDQCEHCXVHGCWRCSURFHVVCLQIRUPDWLRQCLQCDCZDACWKDWCWDNHVCRXUCSHUIRUPDQFHCDQGCFDSDELOLWLHVCWRCDQCHQWLUHOACQHZCOHYHOBCVKDQQRQCOHDUQHGCWKLVCDQGCQRZCXVHVCTXDQWXPCFRPSXWLQJCWRCDGYDQFHCKHUCVHFXULWABCDQDOAVLVBCDQGCVRCPXFKCPRUHBCWHFKQRORJACLVCEHDXWLIXOCEHFDXVHCLWCFRQWLQXHVCWRCRIIHUCVXFKCDPDBLQJCQHZCRSSRUWXQLWLHVB"
    caesar_crack(cipher_text)
