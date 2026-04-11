def sat(n: int):
    for i in range(5):
        assert n % 5 == 1
        n -= 1 + (n - 1) // 5
    return n > 0 and n % 5 == 1

def sol():
    return 0

# The code above will always return 0 because the for loop does not terminate and n is never set to 0.

if __name__ == "__main__":
    assert sat(sol())
