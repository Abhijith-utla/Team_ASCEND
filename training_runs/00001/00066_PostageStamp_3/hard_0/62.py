def sat(stamps: List[int], target=19, max_stamps=2, options=[19, 14, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

assert sat([])
assert not sat([19])
assert not sat([19, 19])
assert not sat([19, 19, 19])
assert not sat([19, 14])
assert sat([14], 19, 1, [14, 19])
assert sat([14, 14], 39, 2, [14, 14, 19])
assert not sat([14, 14, 14], 49, 3, [14, 14, 14, 19])
assert not sat([14, 14, 14, 14], 59, 4, [14, 14, 14, 14, 19])
assert not sat([14, 14, 14, 14, 14], 69, 5, [14, 14, 14, 14, 14, 19])

if __name__ == "__main__":
    assert sat(sol())
