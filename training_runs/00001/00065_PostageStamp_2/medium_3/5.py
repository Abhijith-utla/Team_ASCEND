def sat(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

assert not sat([])
assert not sat([1])
assert not sat([1, 2])
assert not sat([1, 2, 3])
assert not sat([18, 1, 43, 81])
assert not sat([18, 1])
assert not sat([18, 1, 43])
assert not sat([18, 1, 43, 81, 1])
assert not sat([18, 1, 43, 81, 1, 1])
assert not sat([18, 1, 43, 81, 1, 2])
assert sat([18, 1, 43, 81, 1, 2, 2])
assert sat([18, 1, 43, 81, 1, 2, 3])
assert sat([18, 1, 43, 81, 1, 2, 3, 2])
assert sat([18, 1,

if __name__ == "__main__":
    assert sat(sol())
