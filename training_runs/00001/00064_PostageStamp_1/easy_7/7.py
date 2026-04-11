def sat(stamps: List[int], target=271, max_stamps=8, options=[3, 3, 3, 3, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test cases
assert sat([3, 3, 3, 3, 3]) == True
assert sat([3, 3, 3, 3, 4]) == False
assert sat([3, 3, 3, 3, 3], target=271, max_stamps=8) == True
assert sat([3, 3, 3, 3, 3], target=272, max_stamps=8) == False
assert sat([3, 3, 3, 3, 3], target=271, max_stamps=7) == False
assert sat([3, 3, 3, 3, 3], target=271, options=[3, 3, 3, 3, 4]) == False

def sol():
    return []

# Test cases
assert sat([3, 3, 3, 3, 3]) == True
assert sat([3, 3, 3, 3, 4]) == False
assert sat([3, 3

if __name__ == "__main__":
    assert sat(sol())
