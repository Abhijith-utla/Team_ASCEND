def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Incorrect pattern:
def sol(stamps, target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    assert sat(stamps, target, max_stamps, options)
    return stamps

# Incorrect pattern:
def sol(stamps=[37, 37, 12, 87, 39], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    assert sat(stamps, target, max_stamps, options)
    return stamps

# Incorrect pattern:
def sol(stamps=[37, 37, 12, 87, 39], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    assert sat(stamps, target, max_stamps,

if __name__ == "__main__":
    assert sat(sol())
