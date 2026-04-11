def sat(i: int):
    return len(str(i + 1000)) < len(str(i + 1001))

def sol():
    return len(str(int(1e3) + 1000)) < len(str(int(1e3) + 1001))

print(sol())

if __name__ == "__main__":
    assert sat(sol())
