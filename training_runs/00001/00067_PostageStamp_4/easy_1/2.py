def sat(stamps: List[int], target=56, max_stamps=1, options=[25, 22, 8, 84, 60, 56, 54, 7, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return [8, 8, 54, 56]

# Test the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
