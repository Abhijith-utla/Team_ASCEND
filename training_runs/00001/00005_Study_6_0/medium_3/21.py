def sat(i: int):
    return i <= 10 ** 10 and i % 2 == 0

def sol():
    i = 2  # Start from 2 as even number is the first even number
    while i <= 10 ** 10:
        if i % 2 == 0:
            return i

if __name__ == "__main__":
    assert sat(sol())
