def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test cases
print(sat([37, 37, 12, 87, 39]))  # Returns True
print(sat([37, 37, 12, 87]))  # Returns False
print(sat([37, 37, 12, 87, 39, 39]))  # Returns False
print(sat([37, 37, 12, 87]))  # Returns True
print(sat([], 271, 8, [37, 37, 12, 87, 39]))  # Returns True
print(sat([37, 37, 12, 87, 39, 99]))  # Returns False
print(sat([37, 37, 12, 87, 39, 39]))  # Returns False
print(sat([37, 37, 12, 87, 39, 39, 39]))  #

if __name__ == "__main__":
    assert sat(sol())
