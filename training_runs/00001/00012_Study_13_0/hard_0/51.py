def sat(x: float):
    return str(x - 3.1415).startswith("123.456")

def sol():
    return 3.1415

# Testing the correct pattern
assert sat(sol())

# Testing the incorrect pattern
assert not sat(sol() + 1)

# Testing the incorrect pattern
assert not sat(sol() - 1)

# Testing the incorrect pattern
assert not sat(sol() * 2)

# Testing the incorrect pattern
assert not sat(sol() / 2)

if __name__ == "__main__":
    assert sat(sol())
