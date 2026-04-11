def sat(i: int):
    return i <= 10 ** 10 and i % 2 == 0

def sol():
    i = 1
    while i <= 10 ** 10:
        if i % 2 == 0:
            return i
        i += 1

if __name__ == "__main__":
    assert sat(sol())
