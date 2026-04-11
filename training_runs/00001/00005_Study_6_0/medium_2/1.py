def sat(i: int):
    return i % 5 == 0 and i < 100

def sol():
    return 100

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
