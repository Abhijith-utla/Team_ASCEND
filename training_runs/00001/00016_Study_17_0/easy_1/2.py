def sat(i: int):
    return len(str(i + 1000)) == len(str(i + 1001))

def sol():
    for i in range(1000000):  # assuming that i is a non-negative integer
        if len(str(i + 1000)) == len(str(i + 1001)):
            return i

if __name__ == "__main__":
    assert sat(sol())
