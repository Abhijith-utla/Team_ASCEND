def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

def sol():
    i = 1234
    while not sat(i):
        i += 1
    return i

def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

# Test the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
