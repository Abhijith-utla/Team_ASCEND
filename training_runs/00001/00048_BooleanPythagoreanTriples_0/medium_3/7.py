def sat(n: int, m: int, p: int):
    assert n >= 0, 'n must be greater than or equal to 0'
    assert m >= 0, 'm must be greater than or equal to 0'
    assert p >= 0, 'p must be greater than or equal to 0'
    assert n + m + p == m, 'Sum of n, m, and p must equal m'
    return n + m >= p

def sol():
    return 0

# The solution is 0 because when sum of n, m, and p is not equal to m, n and m cannot be both greater than or equal to p. So the function will always return false.

if __name__ == "__main__":
    assert sat(sol())
