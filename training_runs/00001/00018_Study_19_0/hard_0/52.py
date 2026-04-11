def sat(li: List[int]):
    return {i + j for i in li for j in li} == {0, 1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 34}

def sol():
    return set()

# The answer object is a set that is empty.
# This means that the function sol() returned a set that is an empty set.

# The checker will run: assert sat(sol())
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
