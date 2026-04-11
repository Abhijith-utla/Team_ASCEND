def sat(stamps: List[int], target=19):
    unique_stamps = set(stamps)
    for s in unique_stamps:
        if s not in [19, 14, 81]:
            return False
    return len(unique_stamps) <= 2 and sum(stamps) == target

def sol():
    return []

# This code should be adjusted as per your requirements
assert sat([14, 14, 81, 19])
assert not sat([19, 19, 81, 14])
assert not sat([19, 19, 14, 14])
assert sat([14, 14, 14, 14])
assert not sat([19, 19, 19, 14])
assert not sat([81, 81, 14, 14])

if __name__ == "__main__":
    assert sat(sol())
