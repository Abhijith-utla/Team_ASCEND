def sat(n: int, lace="bbbbrr"):
    return lace[n - 1:n + len(lace) // 2] == 'r' * (2 * (n - 1))

def sol():
    return 'bbbbrr'

assert sat(1)
assert not sat(2)
assert sat(3)
assert not sat(4)
assert sat(5)
assert not sat(6)

if __name__ == "__main__":
    assert sat(sol())
