def sat(i: int):
    return len(str(i + 1000)) != len(str(i + 1001))

def sol():
    for i in range(1000, 1100):
        if sat(i):
            return i
    return None

def sat(i: int):
    return len(str(i + 1000)) != len(str(i + 1001))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
