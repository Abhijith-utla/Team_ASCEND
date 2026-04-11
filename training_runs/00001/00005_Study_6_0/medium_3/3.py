def sat(i: int):
    return i <= 10 ** 10 and i % 2 == 0

def sol():
    i = 20  # Start from an even number
    while True:
        if sat(i):
            return i

if __name__ == "__main__":
    assert sat(sol())
