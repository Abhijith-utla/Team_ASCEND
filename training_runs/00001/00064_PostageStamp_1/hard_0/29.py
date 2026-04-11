def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# You can replace the list of stamps and options with your own values
stamps = [37, 37, 12, 87, 39]
options = [37, 37, 12, 87, 39, 271]
max_stamps = 8
target = 271

# Check if the stamps and options satisfy the problem constraints
assert sat(stamps, target, max_stamps, options)

# If the constraints are satisfied, return an empty list
return []

if __name__ == "__main__":
    assert sat(sol())
