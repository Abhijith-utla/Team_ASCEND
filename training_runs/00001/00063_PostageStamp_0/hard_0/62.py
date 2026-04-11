def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# You can test the function by uncommenting the following lines:
# print(sat([10, 10, 10, 10]))  # False
# print(sat([32, 10, 10, 10]))  # False
# print(sat([8, 8, 8, 8]))  # True

def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

if __name__ == "__main__":
    assert sat(sol())
