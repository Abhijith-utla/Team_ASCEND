def sat(i: int):
    return i % 123 == 4 and i > 10 ** 10

def sol():
    return 4

if __name__ == "__main__":
    assert sat(sol())
