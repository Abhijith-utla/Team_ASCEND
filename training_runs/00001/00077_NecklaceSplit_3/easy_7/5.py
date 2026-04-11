def sat(n: int, lace="bbbbrr"):
    return lace[n - 1:n + len(lace) // 2] == 'r' * (2 * (n - 1))

def sol():
    return 0

if __name__ == "__main__":
    assert sat(sol())
