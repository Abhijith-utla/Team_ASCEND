def sat(n: int):
    return lace[n:n + len(lace) // 2] == 'r' * (2 * n + 1)

def sol():
    return 'r' * (2 * 0 + 1)

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
