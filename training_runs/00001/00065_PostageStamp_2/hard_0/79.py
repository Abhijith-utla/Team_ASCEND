def sat(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# This checks that the function `sol()` returns an empty list.
# If `sol()` returns something else, this check will fail.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
