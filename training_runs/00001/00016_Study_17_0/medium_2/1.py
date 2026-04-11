def sat(i: int):
    return len(str(i + 1000)) == len(str(i + 1001))

def sol():
    i = 12345
    return len(str(i + 1000)) == len(str(i + 1001))

if __name__ == "__main__":
    assert sat(sol())
