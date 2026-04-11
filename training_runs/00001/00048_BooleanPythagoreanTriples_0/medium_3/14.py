def sat(n: int, m: int, p: int):
    assert n >= 0, 'n must be greater than or equal to 0'
    assert m >= 0, 'm must be greater than or equal to 0'
    assert p >= 0, 'p must be greater than or equal to 0'
    assert n + m + p == m, 'Sum of n, m, and p must equal m'
    return n + m >= p

def sol():
    return {}

assert sat(1, 2, 3) == False
assert sat(2, 2, 3) == True
assert sat(0, 0, 0) == True
assert sat(1, 0, 1) == False
assert sat(0, 1, 1) == True
assert sat(0, 1, 2) == False

if __name__ == "__main__":
    assert sat(sol())
