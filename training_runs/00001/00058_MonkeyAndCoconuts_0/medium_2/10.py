def sat(n: int):
    for _ in range(5):
        assert n % 5 != 0
        n -= 1
    return n > 0

def sol():
    return -1

# The function sol() returns -1 because the loop in the function sat(n: int) is executed five times and the value of n is not divisible by 5 and is greater than 0 at the end of the loop.

if __name__ == "__main__":
    assert sat(sol())
