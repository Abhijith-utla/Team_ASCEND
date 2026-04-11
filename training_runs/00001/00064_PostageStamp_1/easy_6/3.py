def sat(stamps: List[int], target=271, max_stamps=8, options=[7, 8, 9]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test cases
assert not sat([])
assert not sat([1])
assert not sat([7])
assert sat([7, 7])
assert sat([7, 8])
assert sat([7, 7, 7])
assert not sat([7, 7, 7, 7])
assert not sat([7, 9])
assert sat([7, 9, 9])
assert sat([7, 8, 8])
assert sat([7, 8, 9])
assert sat([7, 8, 9, 9])
assert not sat([7, 8, 8, 9])
assert not sat([7, 8, 9, 9, 9])
assert not sat([7, 8, 9, 8, 9])
assert not sat([9, 8, 8, 8, 7])
assert not sat([9, 9, 9, 9, 8])
assert sat([9, 9, 9, 9, 9])

if __name__ == "__main__":
    assert sat(sol())
