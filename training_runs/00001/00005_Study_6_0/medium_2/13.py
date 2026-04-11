def sat(i: int):
    return i % 5 == 0 and i < 100

def sol():
    i = 0
    while i < 100:
        if i % 5 == 0:
            return i

if __name__ == "__main__":
    assert sat(sol())
