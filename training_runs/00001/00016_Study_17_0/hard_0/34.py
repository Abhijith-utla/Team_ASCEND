def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

def sol():
    i = 1
    while True:
        if sat(i):
            return i
        i += 1

def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
