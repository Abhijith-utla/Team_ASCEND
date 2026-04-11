def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# You can add the solution in the function
# Here is how you can do it:
# Suppose we have a list of stamps: [37, 37, 12, 87, 39]
# If the sum of the stamps is equal to 271 and the number of stamps is less than or equal to 8, return the stamps.
# Otherwise, return an empty list.
def sol():
    return [37, 37, 12, 87, 39]

# If the above list of stamps matches the condition, assert sat(stamps) is true
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
