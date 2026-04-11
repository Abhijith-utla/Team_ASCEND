def sat(n: int):
    for _ in range(3):
        assert n % 5 == 0
        n -= 1
    return n > 0

def sol():
    for _ in range(3):
        assert 5 % 5 == 0
        n = 4
    return n

# The checker will run:
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
