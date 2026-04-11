def sat(n: int):
    for _ in range(7):
        assert n % 5 == 0
        n -= 1
    return n > 0

def sol():
    n = 50
    while n > 0:
        n -= 1
        if n % 5 == 0:
            n -= 1
        if n % 5 == 0:
            n -= 1
        if n % 5 == 0:
            n -= 1
        if n % 5 == 0:
            n -= 1
        if n % 5 == 0:
            n -= 1
        if n % 5 == 0:
            n -= 1
        if n % 5 == 0:
            n -= 1
    return n > 0

# Test cases
assert sat(sol())
!python -m pytest -v test_sat.py

if __name__ == "__main__":
    assert sat(sol())
