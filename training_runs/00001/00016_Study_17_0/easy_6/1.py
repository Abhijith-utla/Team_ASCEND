def sat(i: int) -> bool:
    return len(str(i + 1000)) == len(str(i + 10000))

def sol():
    i = 1000
    while not sat(i):
        i += 1
    return i

if __name__ == "__main__":
    assert sat(sol())
