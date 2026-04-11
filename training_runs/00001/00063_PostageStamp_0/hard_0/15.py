def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Testing
assert sat([])
assert not sat([10])
assert not sat([10, 10])
assert sat([10, 10], 120, 4, [10, 10, 20, 30])
assert not sat([10, 10], 110, 4, [10, 10, 20, 30])
assert not sat([10, 10, 20, 30], 80, 4, [10, 10, 20, 30])
assert sat([10, 10, 20, 30], 80, 4, [10, 10, 20, 30, 40])

if __name__ == "__main__":
    assert sat(sol())
