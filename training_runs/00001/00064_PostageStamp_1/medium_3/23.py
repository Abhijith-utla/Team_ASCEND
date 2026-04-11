def sat(stamps: List[int], target=271, max_stamps=8, options=[3, 3, 3, 3, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test
assert sat([]) == False
assert sat([1]) == False
assert sat([3]) == True
assert sat([3, 3, 3, 3, 3]) == True
assert sat([1, 1, 2]) == False
assert sat([1, 2, 2, 2, 3]) == False
assert sat([1, 1, 1, 1, 3]) == True
assert sat([3, 3, 3, 3, 3]) == True
assert sat([1, 2, 3, 3, 4]) == False
assert sat([1, 1, 1, 1, 1, 2]) == False
assert sat([3, 3, 3, 3, 3, 3, 3]) == False
assert sat([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,

if __name__ == "__main__":
    assert sat(sol())
