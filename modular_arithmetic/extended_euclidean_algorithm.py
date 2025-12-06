# implementation of extended euclidean algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)

    # b % a is always smaller number - and 'a' is the smaller int
    gcd, x1, y1 = egcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


if __name__ == "__main__":
    print(egcd(15, 56))
