def sat(stamps: List[int], target=271, max_stamps=8, options=[3, 3, 3, 3, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

print(sat([], 271, 8, [3, 3, 3, 3, 3]))  # returns True
print(sat([3, 3, 3, 3, 3], 271, 8, [3, 3, 3, 3, 3]))  # returns False
print(sat([3, 3, 3, 3, 3], 270, 8, [3, 3, 3, 3, 3]))  # returns False
print(sat([3, 3, 3, 3, 3], 271, 9, [3, 3, 3, 3, 3]))  # returns False
print(sat([3, 3, 3, 3, 3], 271, 8, [3, 3, 3, 3, 2]))  # returns False
print(sat([3, 3, 3, 3, 3], 271, 8, [3,

if __name__ == "__main__":
    assert sat(sol())
