def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

def sol():
    i = 0
    while True:
        if sat(i):
            return i
        i += 1

def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

# Test the function
assert sol() == 999

if __name__ == "__main__":
    assert sat(sol())
