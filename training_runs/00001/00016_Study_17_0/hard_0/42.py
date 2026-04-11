def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

def sol():
    return len(str(len(str(10**72)) + 1000)) > len(str(len(str(10**73)) + 1001))

print(sol())

if __name__ == "__main__":
    assert sat(sol())
