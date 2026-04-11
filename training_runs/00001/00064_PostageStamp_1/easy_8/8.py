def sat(stamps: List[int], target=271, max_stamps=8, options=[3, 3, 3, 3, 3, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Incorrect pattern:
def sol(x):
    ...

# Correct pattern:
def sol(stamps=[1,1,1,1,1,1,1,1], target=271, max_stamps=8, options=[3, 3, 3, 3, 3, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
