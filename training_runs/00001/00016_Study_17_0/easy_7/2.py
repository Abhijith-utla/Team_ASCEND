def sat(i: int) -> bool:
    return len(str(i + 1000)) < len(str(i + 1001))

def sol():
    return sat(123456789)

# Testing
assert sat(123456789)
assert not sat(123456799)

if __name__ == "__main__":
    assert sat(sol())
