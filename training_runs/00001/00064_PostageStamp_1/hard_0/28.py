def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test
assert sat([37, 37, 12, 87, 39])
assert not sat([37, 37, 12, 87, 30])
assert not sat([37, 37, 12, 87, 40])
assert not sat([37, 37, 12, 87])
assert not sat([37, 37, 12, 80])

if __name__ == "__main__":
    assert sat(sol())
