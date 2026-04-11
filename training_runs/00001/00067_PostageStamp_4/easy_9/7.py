def sat(stamps: List[int], target=56, max_stamps=2, options=[25, 22, 8, 84, 60, 56]):
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Output: [56]
assert sat(sol())

# Output: [25, 22]
assert sat(sol([25, 22]))

# Output: [56]
assert sat(sol([56]))

# Output: [84]
assert sat(sol([84]))

# Output: [60, 56]
assert sat(sol([60, 56]))

# Output: [56, 56]
assert sat(sol([56, 56]))

# Output: [8, 56]
assert sat(sol([8, 56]))

# Output: [22, 56]
assert sat(sol([22, 56]))

# Output: [8, 22, 56]
assert sat(sol([8, 22, 56]))

# Output: [25, 22, 56]
assert sat(sol([25, 22, 56]))

# Output

if __name__ == "__main__":
    assert sat(sol())
