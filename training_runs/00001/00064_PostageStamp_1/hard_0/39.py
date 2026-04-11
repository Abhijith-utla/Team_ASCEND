def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test Case 1
assert sat([37, 37, 12, 87, 39]) == True

# Test Case 2
assert sat([37, 37, 12, 87, 99]) == False

# Test Case 3
assert sat([37, 37, 37, 37, 37]) == True

# Test Case 4
assert sat([1, 1, 1, 1, 1]) == True

# Test Case 5
assert sat([2, 2, 2, 2, 2]) == False

# Test Case 6
assert sat([]) == False

# Test Case 7
assert sat([39, 87, 12, 37, 37]) == True

# Test Case 8
assert sat([39, 87, 87, 37, 12]) == True

# Test Case 9
assert sat([1, 2, 3,

if __name__ == "__main__":
    assert sat(sol())
