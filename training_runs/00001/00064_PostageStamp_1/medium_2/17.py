def sat(stamps: List[int], target=271, max_stamps=8, options=[1, 2, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test case
assert sat([]) == True
assert sat([1, 2, 3]) == False
assert sat([1, 1, 1]) == True
assert sat([1, 2, 3], 50, 3, [1, 2, 3, 5]) == False
assert sat([1, 2, 3], 9, 3, [1, 2, 3, 5]) == False
assert sat([1, 2, 3], 8, 3, [1, 2, 3, 5]) == False
assert sat([1, 2, 3], 7, 2, [1, 2, 3, 5]) == False
assert sat([1, 2, 3], 6, 2, [1, 2, 3, 5]) == False
assert sat([1, 2, 3], 5, 1, [1, 2, 3, 5]) == False
assert sat([1, 2, 3], 4,

if __name__ == "__main__":
    assert sat(sol())
