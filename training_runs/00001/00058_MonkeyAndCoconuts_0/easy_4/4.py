def sat(n: int):
    for _ in range(5):
        assert n % 5 != 0
        n -= 1
    return n > 0

def sol():
    n = 50
    while n > 0:
        n -= 1
    return n

print(sol())

if __name__ == "__main__":
    assert sat(sol())
