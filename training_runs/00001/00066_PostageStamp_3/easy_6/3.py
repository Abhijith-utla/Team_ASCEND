def sat(stamps: List[int], target=19):
    unique_stamps = set(stamps)
    for s in unique_stamps:
        if (s not in [19, 14, 81] and s != target):
            return False
    return len(unique_stamps) <= 1 and sum(stamps) == target

def sol():
    return []

# Testing the solution
assert sat([81, 14, 14, 19])
assert not sat([81, 14, 14, 19, 19])
assert not sat([81, 14, 14])
assert sat([81])
assert not sat([])

if __name__ == "__main__":
    assert sat(sol())
