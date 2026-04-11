def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# The output of the function sol() will be an empty list because the condition is not met
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
