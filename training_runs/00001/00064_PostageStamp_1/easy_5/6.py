def sat(stamps: List[int], target=271, max_stamps=8, options=[4, 5, 6]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# test cases
assert sat([4, 5, 6])
assert not sat([4, 5, 7])
assert not sat([4, 5, 5])
assert sat([4, 4, 4])
assert sat([4, 4, 4, 4])
assert not sat([4, 5, 5, 5])
assert not sat([4, 6, 6, 6])
assert not sat([5, 6, 6, 7])

if __name__ == "__main__":
    assert sat(sol())
