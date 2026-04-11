def sat(i: int):
    return i % 123 == 4 and i > 10 ** 10

def sol():
    i = 1234567891011 # Replace this number with any integer you want
    while not sat(i):
        i += 1
    return i

if __name__ == "__main__":
    assert sat(sol())
