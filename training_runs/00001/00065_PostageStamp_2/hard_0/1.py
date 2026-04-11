def sat(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

# Test cases
print(sol([1, 1, 1, 1], 4, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # True
print(sol([1, 1, 1, 1], 4, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]))  # False
print(sol([1, 1, 1, 1], 4, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))  # False

if __name__ == "__main__":
    assert sat(sol())
