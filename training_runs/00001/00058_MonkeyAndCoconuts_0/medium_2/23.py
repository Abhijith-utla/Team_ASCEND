def sat(n: int):
    for _ in range(5):
        assert n % 5 != 0
        n -= 1
    return n > 0

def sol():
    n = 95
    while n % 5 == 0:
        n -= 1
    return n

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
