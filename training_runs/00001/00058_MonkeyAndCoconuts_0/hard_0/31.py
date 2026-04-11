def sat(n: int):
    for i in range(5):
        assert n % 5 == 1
        n -= 1 + (n - 1) // 5
    return n > 0 and n % 5 == 1

def sol():
    n = 25
    for i in range(5):
        assert n % 5 == 1
        n -= 1 + (n - 1) // 5
    return n

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
