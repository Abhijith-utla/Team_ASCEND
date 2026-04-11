def sat(n: int):
    for i in range(5):
        assert n % 5 == 1
        n -= 1 + (n - 1) // 5
    return n > 0 and n % 5 == 1

def sol():
    n = 100
    while n > 0:
        n -= 1 + (n - 1) // 5
        if n % 5 == 1:
            break
    else:
        n = -1
    return n

# assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
