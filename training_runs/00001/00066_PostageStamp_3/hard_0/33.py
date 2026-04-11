def sat(stamps: List[int], target=19, max_stamps=2, options=[19, 14, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return [19, 14, 81]

# Asserts
assert sat([19, 14, 81])
assert not sat([19, 14])
assert not sat([19, 14, 99])

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
