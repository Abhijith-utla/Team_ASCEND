def sat(i: int) -> bool:
    return i < (i + 1)

def sol():
    return 4

if __name__ == "__main__":
    assert sat(sol())
