def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test case
assert sat([10, 32, 8])
assert not sat([10, 10, 10, 10])
assert not sat([32, 8, 8])
assert not sat([10, 32])
assert not sat([], target=80, max_stamps=4, options=[10, 32, 8])

# Correct pattern
def sol():
    return [10, 32, 8]

if __name__ == "__main__":
    assert sat(sol())
