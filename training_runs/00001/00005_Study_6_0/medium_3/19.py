def sat(i: int):
    return i <= 10 ** 10 and i % 2 == 0

def sol():
    return 2  # Since 2 is the only even number less than or equal to 10 ** 10

if __name__ == "__main__":
    assert sat(sol())
