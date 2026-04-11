def sat(i: int):
    return i <= 10 ** 10 and i % 2 == 0

def sol():
    return 2000000000

if __name__ == "__main__":
    assert sat(sol())
