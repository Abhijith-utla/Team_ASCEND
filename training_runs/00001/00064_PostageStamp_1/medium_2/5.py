def sat(stamps: List[int], target=271, max_stamps=8, options=[1, 2, 3]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
