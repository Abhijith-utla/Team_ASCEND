def sat(n: int, m: int, p: int):
    assert n >= 0, 'n must be greater than or equal to 0'
    assert m >= 0, 'm must be greater than or equal to 0'
    assert p >= 0, 'p must be greater than or equal to 0'
    assert n + m + p == m, 'Sum of n, m, and p must equal m'
    return n + m >= p

def sol():
    return (0, 0, 0)

# This will test the function with the following inputs:
# (0, 0, 0)
# (1, 0, 0)
# (0, 1, 0)
# (0, 0, 1)
# (1, 1, 1)
# (2, 2, 2)
# (1, 2, 3)
# (5, 6, 7)

# You can run these tests by calling the function and checking the returned values:
assert sol() == (0, 0, 0)
assert sol(1, 0, 0) == (1, 0, 0)
assert sol(0, 1, 0) == (1, 1, 1)
assert sol(0, 0, 1) == (1, 1, 2)
assert sol(1, 1, 1) == (1, 2, 3)
assert sol(2, 2, 2) == (2, 4,

if __name__ == "__main__":
    assert sat(sol())
