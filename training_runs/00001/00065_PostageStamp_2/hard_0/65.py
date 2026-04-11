def sat(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# This test should be valid
assert sat([18, 1, 43, 81])

# This test should fail
assert not sat([18, 1, 43])

# This test should fail
assert not sat([18, 1, 44])

# This test should fail
assert not sat([18, 100, 43])

# This test should fail
assert not sat([18, 100, 44])

# This test should pass
assert sat([18, 1, 43, 81])

if __name__ == "__main__":
    assert sat(sol())
