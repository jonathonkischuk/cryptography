def modular_inverse(a, m):
    # brute-force approach
    # m may be too large (1024 bits long prime number)
    # run time seems to be O(m) linear, but actually exponential
    for inv in range (0, m):
        if (a * inv) % m == 1:
            return inv

    print("No Modular Inverse (a is not coprime to m)")


if __name__ == "__main__":
    print(modular_inverse(9, 31))
    