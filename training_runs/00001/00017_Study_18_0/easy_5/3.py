def sat(a: int, b: int) -> bool:
    return a + b == 5

def sol():
    return 2

# Test case 1
assert sat(1, 4)
# Test case 2
assert not sat(3, 3)

if __name__ == "__main__":
    assert sat(sol())
