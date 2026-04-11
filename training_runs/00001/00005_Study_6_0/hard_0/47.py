def sat(i: int):
    return i % 123 == 4 and i > 10 ** 10

def sol():
    for i in range(10000000000, 123000000000):
        if sat(i):
            return i

if __name__ == "__main__":
    assert sat(sol())
