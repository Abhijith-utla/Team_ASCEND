def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    if len(stamps) > max_stamps:
        return False
    for s in stamps:
        if s not in options:
            return False
    return sum(stamps) == target

def sol():
    return []

# This line is for testing purposes only and not part of the solution.
assert sat([])
assert not sat([10])
assert not sat([10, 10])
assert sat([10, 10, 10, 10])
assert not sat([10, 10, 11])
assert not sat([10, 32, 8])
assert sat([10, 32, 8, 1])
assert not sat([10, 32, 8, 1, 1])

if __name__ == "__main__":
    assert sat(sol())
