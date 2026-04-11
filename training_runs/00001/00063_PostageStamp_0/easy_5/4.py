def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    if len(stamps) > max_stamps:
        return False
    for s in stamps:
        if s not in options:
            return False
    return sum(stamps) == target

def sol():
    return []

# If the function `sat` is not provided by the user,
# Python's built-in `assert` statement will fail.
# So, if `sat` is not defined, the function `sol` should return an empty list.
assert sat([])

# Let's test our solution with some examples:
assert not sol([])
assert not sol([32])
assert not sol([32, 32])
assert not sol([32, 32, 32, 32])
assert sol([10, 32, 8])
assert sol([10, 10, 32, 8])
assert not sol([10, 10, 10, 10])
assert not sol([10, 10, 10, 33])

if __name__ == "__main__":
    assert sat(sol())
