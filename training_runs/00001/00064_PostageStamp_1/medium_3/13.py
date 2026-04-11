def sat(stamps: List[int], target=271, max_stamps=8, options=[3, 3, 3, 3, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Testing the function
assert sat([])
assert not sat([3])
assert sat([3, 3, 3, 3, 3])
assert not sat([3, 3, 3, 3, 4])
assert sat([3, 3, 3, 3, 3], 271, 8, [3, 3, 3, 3, 3])
assert not sat([3, 3, 3, 3, 3], 270, 8, [3, 3, 3, 3, 3])

# Defining the final function
def sol():
    return [3, 3, 3, 3, 3]

if __name__ == "__main__":
    assert sat(sol())
