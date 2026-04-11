def sat(n: int):
    for _ in range(5):
        assert n % 5 != 0
        n -= 1
    return n > 0

def sol():
    n = 100
    while n > 0:
        if sat(n):
            return n
        n -= 1

    assert False  # This line will never run as n > 0 is not guaranteed

if __name__ == "__main__":
    assert sat(sol())
