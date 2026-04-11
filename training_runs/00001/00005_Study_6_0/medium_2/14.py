def sat(i: int):
    return i % 5 == 0 and i < 100

def sol():
    for i in range(100):
        if sat(i):
            return i

if __name__ == "__main__":
    assert sat(sol())
