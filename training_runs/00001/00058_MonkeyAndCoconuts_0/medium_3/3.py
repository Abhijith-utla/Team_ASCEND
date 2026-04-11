def sat(n: int):
    for _ in range(3):
        assert n % 5 == 0
        n -= 1
    return n > 0

def sol():
    n = 100
    while n > 0:
        if sat(n):
            return n
        n -= 1
    return 0

print(f"The final answer is {sol()}")

if __name__ == "__main__":
    assert sat(sol())
