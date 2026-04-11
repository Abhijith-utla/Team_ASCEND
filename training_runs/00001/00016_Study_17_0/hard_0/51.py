def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

def sol():
    for i in range(10000000000000):
        if sat(i):
            return i
    return None

print(sol())

if __name__ == "__main__":
    assert sat(sol())
