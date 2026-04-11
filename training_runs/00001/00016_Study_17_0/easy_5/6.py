def sat(i: int) -> bool:
    return len(str(i + 10)) == len(str(i + 100))

def sol():
    i = 0
    while not sat(i):
        i += 1
    return i

if __name__ == "__main__":
    assert sat(sol())
