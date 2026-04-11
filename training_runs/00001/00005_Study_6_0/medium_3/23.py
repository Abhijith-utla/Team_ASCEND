def sat(i: int):
    return i <= 10 ** 10 and i % 2 == 0

def sol():
    for i in range(-10 ** 10, 10 ** 10):
        if sat(i):
            return i

if __name__ == "__main__":
    assert sat(sol())
