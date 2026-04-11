def sat(ls, idx1=None, idx2=None, value=None):
    if idx1 is None or idx2 is None or value is None:
        return False  # If any of the indices or value is None, it cannot be correct
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    return []

# Test cases
assert sat(sol(), 0, 1, 1)
assert not sat(sol(), 0, 1, 2)
assert not sat(sol(), 0, 2, 1)
assert not sat(sol(), 0, 2, 2)
assert sat(sol(), 1, 2, 1)
assert not sat(sol(), 1, 2, 2)
assert not sat(sol(), 2, 3, 1)
assert not sat(sol(), 2, 3, 2)
assert sat(sol(), 3, 4, 1)
assert not sat(sol(), 3, 4, 2)
assert not sat(sol(), 4, 5, 1)
assert not sat(sol(), 4, 5, 2)
assert not sat(sol(), 5, 6, 1)
assert not sat(sol(), 5, 6, 2)

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
