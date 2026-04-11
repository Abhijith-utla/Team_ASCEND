def sat(stamps: List[int], target=271, max_stamps=8, options=[4, 5, 6]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# This will fail because no stamps are provided
assert sat()

# This will fail because 3 stamps exceed the limit of 8, and their sum is not 271
assert not sat([4, 5, 6, 7, 8, 9, 10, 11])

# This will fail because 2 stamps exceed the limit of 8, and their sum is not 271
assert not sat([4, 5, 6, 7, 8, 9])

# This will pass because 4 stamps are less than or equal to 8, their sum is 271
assert sat([4, 5, 6, 7, 8, 9, 10, 11])

if __name__ == "__main__":
    assert sat(sol())
