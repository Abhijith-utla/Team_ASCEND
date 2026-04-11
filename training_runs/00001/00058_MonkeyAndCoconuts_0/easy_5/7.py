def sat(n: int):
    for _ in range(6):
        assert n % 5 != 0
        n -= 1
    return n > 0

def sol():
    n = 100
    for _ in range(6):
        assert sat(n)
        n -= 1
    return n

if __name__ == "__main__":
    assert sat(sol())
