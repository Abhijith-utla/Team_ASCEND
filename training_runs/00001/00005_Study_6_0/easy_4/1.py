def sat(i: int):
    return i % 5 == 0

def sol():
    i = 0
    while i % 5 != 0:
        i += 1
    return i

if __name__ == "__main__":
    assert sat(sol())
