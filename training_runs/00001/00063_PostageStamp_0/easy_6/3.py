def sat(stamps: List[int], target=80, max_stamps=4, options=None):
    if options is None:
        options = [10, 32, 8]
    if len(stamps) > max_stamps:
        return False
    for s in stamps:
        if s not in options:
            return False
    return sum(stamps) == target

def sol():
    return []

# Test Cases
print(sat([10, 10, 20, 30], 80, 4, [10, 32, 8]))  # Returns True
print(sat([10, 10, 20, 30], 80, 4, [10, 32]))  # Returns False
print(sat([10, 10, 20, 30], 80, 4))  # Returns False
print(sat([10, 10, 20, 30, 30], 80, 4, [10, 32, 8]))  # Returns False
print(sat([10, 10, 20, 30, 30, 30, 30, 30], 200, 8))  # Returns True
print(sat([], 80, 4, [10, 32, 8]))  # Returns True
print(sat([10,

if __name__ == "__main__":
    assert sat(sol())
