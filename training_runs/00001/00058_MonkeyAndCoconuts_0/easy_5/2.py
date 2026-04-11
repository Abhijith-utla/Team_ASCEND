def sat(n: int):
    for _ in range(6):
        assert n % 5 != 0
        n -= 1
    return n > 0

def sol():
    return 1

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
