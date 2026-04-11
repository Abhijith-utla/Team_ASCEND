def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# This is an assertion that will fail if the function `sol` is not correct.
assert sat([])

if __name__ == "__main__":
    assert sat(sol())
