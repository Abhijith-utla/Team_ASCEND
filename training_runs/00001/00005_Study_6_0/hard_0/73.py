def sat(i: int):
    return i % 123 == 4 and i > 10 ** 10

def sol():
    i = 0
    while True:
        i += 1
        if sat(i):
            return i

if __name__ == "__main__":
    assert sat(sol())
