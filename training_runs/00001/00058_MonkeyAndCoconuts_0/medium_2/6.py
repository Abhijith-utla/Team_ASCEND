def sat(n: int):
    for _ in range(5):
        assert n % 5 != 0
        n -= 1
    return n > 0

def sol():
    n = 99
    while n > 0:
        if sat(n):
            return n
        n -= 1

def sat(n: int):
    for _ in range(5):
        assert n % 5 != 0
        n -= 1
    return n > 0

print(sol())

if __name__ == "__main__":
    assert sat(sol())
