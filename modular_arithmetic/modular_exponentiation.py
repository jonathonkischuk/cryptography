from math import sqrt
from math import floor
import random
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[{func.__name__}] time: {end - start:.6f}sec")
        return result
    return wrapper


# Naive approach has an exponential running time complexity
@timeit
def is_prime_naive(num):
    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for n in range(3, floor(sqrt(num))+1, 2):
        if num % n == 0:
            return False
    return True


@timeit
def is_prime_fermat(n, k=10):
    if n <= 1:
        return False

    for _ in range(k):
        a = random.randint(2, n) - 1
        if pow(a, n, n) != a:
            return False

    return True


@timeit
def get_factors(num):
    factors = []
    limit = sqrt(num)

    for n in range(2, floor(limit)):
        if num % n == 0:
            factors.append([n, num/n])

    return factors


@timeit
def discrete_logarithm(a, b, m):
    c = 1
    while pow(b, c) % m != a:
        c = c + 1

    return c


@timeit
def modular_exponentiation(b, c, m):
    return pow(b, c) % m


if __name__ == '__main__':
    print("Naive: ", is_prime_naive(11))

    print("Fermat: ", is_prime_fermat(101))

    print("Factors: ", get_factors(210))

    print("Modular Exponentiation: ", modular_exponentiation(5, 948603, 90))

    print("Discrete Logarithm: ", discrete_logarithm(3668993056, 5, 90))
