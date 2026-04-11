def sat(n: int, lace="bbrrbbrrbbrr"):
    return lace[n - 1:n + len(lace) // 2] == 'r' * (2 * (n - 1))

def sol():
    return 20

assert sat(20)

if __name__ == "__main__":
    assert sat(sol())
