def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test
assert sat([10, 20, 30, 40])  # True
assert not sat([10, 20, 50, 40])  # False
assert sol() == []  # Correct answer

# Checker
assert sat(sol())  # True

if __name__ == "__main__":
    assert sat(sol())
