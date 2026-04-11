def sat(stamps: List[int], target=19):
    unique_stamps = set(stamps)
    for s in unique_stamps:
        if (s not in [19, 14, 81] and s != target):
            return False
    return len(unique_stamps) <= 1 and sum(stamps) == target

def sol():
    return [19, 14, 81]

# Test the solution
print(sol())
assert sat(sol())

# Test with a different solution
print(sol([19, 14, 81]))
assert sat(sol([19, 14, 81]))

# Test with an incorrect solution
print(sol([19, 13, 81]))
assert not sat(sol([19, 13, 81]))

# Test with a different correct solution
print(sol([81, 14]))
assert sat(sol([81, 14]))

if __name__ == "__main__":
    assert sat(sol())
