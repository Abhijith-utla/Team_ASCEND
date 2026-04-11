def sat(i: int):
    return i > 0 and i % 2 == 0

def sol():
    def sat(i: int):
        return i > 0 and i % 2 == 0

    i = 0
    while not sat(i):
        i += 1
    return i

if __name__ == "__main__":
    assert sat(sol())
