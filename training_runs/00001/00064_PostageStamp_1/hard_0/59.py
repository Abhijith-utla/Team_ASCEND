def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

assert not sat([])
assert not sat([37])
assert sat([37, 37])
assert sat([37, 37, 12])
assert sat([37, 37, 12, 87])
assert not sat([37, 37, 12, 87, 39])
assert sat([37, 37, 37])
assert sat([37, 37, 37, 37])
assert not sat([37, 37, 37, 37, 37])
assert sat([37, 37, 37, 37, 12])
assert not sat([37, 37, 37, 37, 12, 87])
assert not sat([37, 37, 37, 37, 12, 87, 39])

if __name__ == "__main__":
    assert sat(sol())
