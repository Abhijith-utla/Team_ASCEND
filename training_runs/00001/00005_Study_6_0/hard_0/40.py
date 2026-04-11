def sat(i: int):
    return i % 123 == 4 and i > 10 ** 10

def sol():
    for i in range(1, 10 ** 10 + 1):
        if sat(i):
            return i
    return None

def sat(i: int):
    return i % 123 == 4 and i > 10 ** 10

print(sol())

if __name__ == "__main__":
    assert sat(sol())
