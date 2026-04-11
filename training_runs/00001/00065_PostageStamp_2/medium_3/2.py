def sat(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# The solution function does not take any arguments
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
