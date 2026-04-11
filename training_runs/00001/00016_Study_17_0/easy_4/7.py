def sat(i: int) -> bool:
    return len(str(i + 1)) == len(str(i + 2))

def sol():
    i = 0
    while not sat(i):
        i += 1
    return i

if __name__ == "__main__":
    assert sat(sol())
