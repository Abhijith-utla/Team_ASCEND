def sat(i: int) -> bool:
    return i < (i + 1)

def sol():
    i = 0
    while sat(i):
        i += 1
    return i

def sat(i: int) -> bool:
    return i < (i + 1)

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
