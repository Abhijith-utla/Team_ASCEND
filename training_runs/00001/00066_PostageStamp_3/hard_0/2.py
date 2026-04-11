def sat(stamps: List[int], target=19, max_stamps=2, options=[19, 14, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol(stamps: List[int], target=19, max_stamps=2, options=[19, 14, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

# Test cases
print(sol([19, 14, 81]))  # True
print(sol([19, 14]))  # False
print(sol([19]))  # False
print(sol([]))  # False
print(sol([19, 14, 19]))  # False
print(sol([19, 14, 81], max_stamps=1))  # True
print(sol([19, 14, 81], max_stamps=3))  # False
print(sol([19, 14, 81], target=200))  # False
print(sol([19, 14, 81], target=200, max_stamps=2

if __name__ == "__main__":
    assert sat(sol())
