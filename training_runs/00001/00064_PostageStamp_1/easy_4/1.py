def sat(stamps: List[int], target=271, max_stamps=8, options=[1, 2, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test case
assert sat([1, 1, 1, 1, 2, 3, 4, 7])
assert not sat([1, 1, 1, 1, 2, 3, 4, 8])
assert sat([1, 1, 1, 1, 1, 1, 1, 1])
assert not sat([1, 1, 1, 1, 1, 1, 1, 2])
assert sat([1, 2, 3, 4, 7])
assert not sat([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2])

if __name__ == "__main__":
    assert sat(sol())
