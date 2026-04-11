def sat(stamps: List[int], target=271, max_stamps=8, options=[3, 3, 3, 3, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test cases
print(sol([3, 3, 3, 3, 3], 271, 8, [3, 3, 3, 3, 3]))  # True
print(sol([3, 3, 3, 3, 2], 271, 8, [3, 3, 3, 3, 3]))  # False
print(sol([3, 3, 3, 3, 3], 272, 8, [3, 3, 3, 3, 3]))  # False
print(sol([3, 3, 3, 3, 3], 271, 9, [3, 3, 3, 3, 3]))  # False

# Checker code
assert sat([3, 3, 3, 3, 3])  # True
assert not sat([3, 3, 3, 3, 2])  # False
assert not sat([3, 3, 3, 3

if __name__ == "__main__":
    assert sat(sol())
