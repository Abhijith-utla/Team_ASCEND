def sat(i: int):
    return i <= 10 ** 10 and i % 2 == 0

def sol():
    return 2 * (10 ** 10)

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
