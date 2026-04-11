def sat(i: int):
    return len(str(i + 1000)) < len(str(i + 1001))

def sol():
    return len(str(1000)) < len(str(1001))

# Test the solution
assert sat(1000)
assert not sat(1001)

if __name__ == "__main__":
    assert sat(sol())
