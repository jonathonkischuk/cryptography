# recursive implementation
def gcd(a, b):
    if a % b == 0:
        return b

    return gcd(b, a % b)


def dcd_iter(a, b):
    while a % b != 0:
        a, b = b, a % b

    return b


if __name__ == '__main__':
    print(gcd(2455, 3965))

    print(dcd_iter(2455, 3965))