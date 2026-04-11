def sat(n: int):
    for _ in range(3):
        assert n % 5 == 0
        n -= 1
    return n > 0

def sol():
    for _ in range(3):
        assert 30 % 5 == 0
        30 -= 1
    return 30

if __name__ == "__main__":
    assert sat(sol())
