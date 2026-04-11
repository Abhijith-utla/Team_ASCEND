def sat(i: int) -> bool:
    return i < (i + 1)

def sol():
    i = 0
    while not sat(i):
        i += 1
    return i

if __name__ == "__main__":
    assert sat(sol())
