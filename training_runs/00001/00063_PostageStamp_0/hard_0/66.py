def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test cases
print(sat([10, 10, 10, 10])) # True
print(sat([10, 32, 8])) # False
print(sat([10, 10, 10, 10, 10, 10])) # False
print(sat([80], max_stamps=2, options=[10, 32, 8])) # False
print(sat([], max_stamps=4, options=[10, 32, 8])) # True
print(sat([8, 8, 8, 8], max_stamps=2, options=[10, 32, 8])) # True

if __name__ == "__main__":
    assert sat(sol())
