def sat(n: int):
    for _ in range(3):
        assert n % 5 == 0
        n -= 1
    return n > 0

def sol():
    n = 10
    while n > 0:
        if n % 5 == 0:
            n -= 1
        else:
            n += 1
    return n

print(sol())

if __name__ == "__main__":
    assert sat(sol())
