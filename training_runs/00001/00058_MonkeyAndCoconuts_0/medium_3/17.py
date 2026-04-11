def sat(n: int):
    for _ in range(3):
        assert n % 5 == 0
        n -= 1
    return n > 0

def sol():
    for _ in range(3):
        assert 10 % 5 == 0
        n = 10 - 1
    return n > 0

# The answer to the problem is:
print(sol())

if __name__ == "__main__":
    assert sat(sol())
