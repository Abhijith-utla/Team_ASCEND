def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

assert sat([])
assert not sat([10])
assert not sat([10, 10])
assert not sat([10, 10, 10, 10])
assert not sat([10, 10, 10, 10], 80, 2, [10, 10, 10, 10])
assert not sat([10, 10, 10, 10], 70, 2, [10, 10, 10, 10])
assert sat([10, 10, 32, 8], 80, 4, [10, 10, 32, 8])
assert not sat([10, 10, 32, 8], 70, 4, [10, 10, 32, 8])

if __name__ == "__main__":
    assert sat(sol())
