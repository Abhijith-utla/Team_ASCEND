def sat(stamps: List[int], target=271, max_stamps=8, options=[3, 3, 3, 3, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

assert sat([])
assert not sat([3]), 'Incorrect stamp count.'
assert not sat([3, 3]), 'Incorrect stamp count.'
assert not sat([3, 3, 3]), 'Incorrect stamp count.'
assert not sat([3, 3, 3, 3, 3]), 'Incorrect stamp count.'
assert not sat([3, 3, 3, 3, 3, 3, 3, 3]), 'Incorrect stamp count.'
assert sat([3, 3, 3, 3, 3]), 'Incorrect total.'
assert not sat([3, 3, 3, 3, 3, 3, 3, 3, 3]), 'Incorrect total.'
assert not sat([1, 2, 3, 4, 5]), 'Incorrect target.'
assert not sat([1, 1, 1, 1, 1, 1, 1, 1]), 'Incorrect max stamps.'
assert sat([1, 2

if __name__ == "__main__":
    assert sat(sol())
