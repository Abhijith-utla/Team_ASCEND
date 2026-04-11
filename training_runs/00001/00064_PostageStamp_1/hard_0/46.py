def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# To satisfy the function `sat`, you need to create a list of stamps that add up to 271.
# The list should contain either 37, 37, 12, 87, or 39 and should not exceed the maximum number of stamps that can be used (8).
# Here's one possible solution:

def sol():
    return [37, 37, 37, 37, 37, 12, 12, 12]

# The test to verify the solution
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
