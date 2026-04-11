def sat(i: int):
    return i > 0 and i % 2 == 0

def sol():
    return 12

if __name__ == "__main__":
    assert sat(sol())
