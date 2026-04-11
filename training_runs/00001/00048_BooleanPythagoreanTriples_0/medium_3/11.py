def sat(n: int, m: int, p: int):
    assert n >= 0, 'n must be greater than or equal to 0'
    assert m >= 0, 'm must be greater than or equal to 0'
    assert p >= 0, 'p must be greater than or equal to 0'
    assert n + m + p == m, 'Sum of n, m, and p must equal m'
    return n + m >= p

def sol():
    return 0

# To pass the test, you can change the values of n, m, and p such that n + m + p = m
n = 1
m = 2
p = 3
assert sat(n, m, p)

# You can also modify the values of n, m, and p to pass the test
n = 2
m = 3
p = 4
assert sat(n, m, p)

if __name__ == "__main__":
    assert sat(sol())
