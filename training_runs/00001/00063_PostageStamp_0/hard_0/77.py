def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

assert not sat([])
assert not sat([10])
assert sat([10, 10])
assert not sat([10, 10, 20])
assert sat([10, 10, 10, 10])
assert not sat([10, 10, 10, 20])
assert not sat([10, 20, 30])
assert sat([10, 32, 8, 5])
assert not sat([5, 5, 5, 5])
assert sat([10, 32, 18, 3])
assert not sat([10, 32, 18, 18])

if __name__ == "__main__":
    assert sat(sol())
