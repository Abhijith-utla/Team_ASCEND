def sat(n: int, m: int, p: int) -> bool:
    assert n >= 0, 'n must be greater than or equal to 0'
    assert m >= 0, 'm must be greater than or equal to 0'
    assert p >= 0, 'p must be greater than or equal to 0'
    assert n + m + p == m, 'Sum of n, m, and p must equal m'
    return n + m >= p

def sol():
    return {
        'n': 0,
        'm': 0,
        'p': 0
    }

if __name__ == "__main__":
    assert sat(sol())
