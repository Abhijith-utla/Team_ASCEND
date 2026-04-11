def sat(i: int):
    return i % 123 == 4 and i > 10 ** 10

def sol():
    i = 10 ** 11
    while i % 123 != 4 or i <= 10 ** 10:
        i += 1
    return i

if __name__ == "__main__":
    assert sat(sol())
