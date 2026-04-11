def sat(stamps: List[int], target=19, max_stamps=2, options=[19, 14, 81]):
    unique_stamps = set(stamps)
    for s in unique_stamps:
        if s not in options:
            return False
    return len(unique_stamps) <= max_stamps and sum(stamps) == target

def sol():
    return [19, 19, 19]

# Test case
assert sat([19, 19, 19])
assert not sat([19, 14, 81])
assert sat([19, 19, 19, 19])
assert not sat([19, 14, 81, 19])
assert not sat([19, 19, 19, 19, 14, 14])
assert sat([19, 19, 19, 14, 14])

if __name__ == "__main__":
    assert sat(sol())
