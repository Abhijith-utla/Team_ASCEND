def sat(stamps: List[int], target=271, max_stamps=8, options=[7, 8, 9]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
