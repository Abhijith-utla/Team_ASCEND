def sat(n: int):
    for _ in range(n):
        assert n % 5 == 0
        n -= 1
    return n > 0

def sol():
    return 0

if __name__ == "__main__":
    assert sat(sol())
