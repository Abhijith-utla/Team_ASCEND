def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

def sol():
    i = 100000000000000000
    while True:
        i += 1
        if len(str(i + 1000)) > len(str(i + 1001)):
            return i

if __name__ == "__main__":
    assert sat(sol())
