def sat(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# assert sat([])
# assert not sat([1, 1, 1])
# assert not sat([1, 1, 2])
# assert sat([1, 1, 3])
# assert not sat([1, 2, 3])
# assert sat([1, 1, 1, 1])
# assert not sat([1, 2, 3, 4])
# assert sat([1, 1, 1, 1, 1])
# assert sat([1, 2, 3, 5])
# assert not sat([1, 2, 3, 7])
# assert sat([1, 1, 1, 1, 1, 1])
# assert not sat([1, 2, 3, 5, 7])
# assert sat([1, 1, 1, 1, 1, 1, 1])
# assert not sat([1, 1, 2, 3, 5, 7])
# assert sat([1, 1,

if __name__ == "__main__":
    assert sat(sol())
