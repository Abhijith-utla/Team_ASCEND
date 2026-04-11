def sat(stamps: List[int], target=271, max_stamps=8, options=[1, 2, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test cases
print(sat([1, 2, 3], 271, 8, [1, 2, 3])) # Returns: True
print(sat([3, 3, 3], 271, 8, [1, 2, 3])) # Returns: False
print(sat([1, 1, 1, 1], 271, 8, [1, 2, 3])) # Returns: False
print(sat([3, 2, 1], 271, 6, [1, 2, 3])) # Returns: True
print(sat([], 271, 8, [1, 2, 3])) # Returns: True
print(sat([1, 2, 3, 4, 5, 6, 7, 8], 56, 8, [1, 2, 3, 4, 5, 6, 7])) # Returns: True
print(sat([1, 2, 3, 4, 5

if __name__ == "__main__":
    assert sat(sol())
