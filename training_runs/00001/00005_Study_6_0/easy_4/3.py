def sat(i: int):
    return i % 5 == 0

def sol():
    return sat(4)

if __name__ == "__main__":
    assert sat(sol())
