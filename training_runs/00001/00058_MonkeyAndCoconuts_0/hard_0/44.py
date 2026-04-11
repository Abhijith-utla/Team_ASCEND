def sat(n: int):
    for i in range(5):
        assert n % 5 == 1
        n -= 1 + (n - 1) // 5
    return n > 0 and n % 5 == 1

def sol():
    n = 100
    while n > 0:
        if sat(n):
            return n
        n -= 1
    return 0

print(sol())

if __name__ == "__main__":
    assert sat(sol())
