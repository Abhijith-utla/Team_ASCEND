def sat(i: int) -> bool:
    return len(str(i)) < len(str(i + 1))

def sol():
    i = 1
    while not sat(i):
        i += 1
    return i

if __name__ == "__main__":
    assert sat(sol())
