def sat(n: int, m: int, p: int):
    assert n >= 0, 'n must be greater than or equal to 0'
    assert m >= 0, 'm must be greater than or equal to 0'
    assert p >= 0, 'p must be greater than or equal to 0'
    assert n + m + p == m, 'Sum of n, m, and p must equal m'
    return n + m >= p

def sol():
    return None

# Test the solution
assert sat(1, 1, 1)
assert not sat(1, 2, 1)
assert not sat(1, 1, 2)
assert not sat(1, 1, 1)
assert not sat(-1, -1, -1)
assert not sat(-1, 0, 0)

if __name__ == "__main__":
    assert sat(sol())
