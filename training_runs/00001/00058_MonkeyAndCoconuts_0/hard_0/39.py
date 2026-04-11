def sat(n: int):
    for i in range(5):
        assert n % 5 == 1
        n -= 1 + (n - 1) // 5
    return n > 0 and n % 5 == 1

def sol():
    n = 1
    while n > 0:
        if n % 5 == 1:
            return n
        n -= 1 + (n - 1) // 5

# Final checker will run:
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
