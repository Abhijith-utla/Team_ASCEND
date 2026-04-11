def sat(i: int):
    return i % 123 == 4 and i > 10 ** 10

def sol():
    i = 10 ** 11
    while True:
        if sat(i):
            return i
        i += 1

if __name__ == "__main__":
    assert sat(sol())
