def sat(i: int):
    return len(str(i + 1000)) < len(str(i + 1001))

def sol():
    i = 123456
    while not sat(i):
        i += 1
    return i

if __name__ == "__main__":
    assert sat(sol())
