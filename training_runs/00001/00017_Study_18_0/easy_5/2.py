def sat(a: int, b: int) -> bool:
    return a + b == 5

def sol():
    return 5

# Test case
assert sat(3, 2)
assert not sat(4, 1)

if __name__ == "__main__":
    assert sat(sol())
