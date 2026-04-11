def sat(ls, idx1=None, idx2=None, value=None):
    if idx1 is None or idx2 is None or value is None:
        return False  # If any of the indices or value is None, it cannot be correct
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    return []

# Test case 1: Correct
assert sat([1, 2, 3, 4, 5], 0, 2, 3) == True
assert sat(['a', 'b', 'c'], 1, 2, 'b') == True
assert sat([True, False, True], 0, 2, False) == True

# Test case 2: Incorrect
assert sat([1, 2, 3, 4, 5], 0, 2, 6) == False
assert sat(['a', 'b', 'c'], 1, 2, 'd') == False
assert sat([True, False, True], 0, 2, True) == False
assert sat([1, 2, 3, 4, 5], 0, 2, None) == False  # If value is None
assert sat(['a', 'b', 'c'], 1, 2, 'a') == False  # If idx1 and idx2 are the same
assert sat([True, False, False], 0, 1, True

if __name__ == "__main__":
    assert sat(sol())
