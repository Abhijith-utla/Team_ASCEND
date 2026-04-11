def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return [37, 37, 12, 87, 39]

# Assertion to ensure the function works
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
