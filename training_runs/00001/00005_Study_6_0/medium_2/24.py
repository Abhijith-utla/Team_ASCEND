def sat(i: int):
    return i % 5 == 0 and i < 100

def sol():
    return 5 in range(100)

if __name__ == "__main__":
    assert sat(sol())
