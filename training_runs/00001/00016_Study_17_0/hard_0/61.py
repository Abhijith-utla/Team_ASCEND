def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

def sol():
    return len(str(int(1e9) + 1000)) > len(str(int(1e9) + 1001))

# Test the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
