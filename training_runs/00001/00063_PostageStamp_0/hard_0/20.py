def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# assert sat([])
# assert not sat([10])
# assert not sat([10, 10])
# assert not sat([10, 30])
# assert sat([10, 30], target=80, max_stamps=4, options=[10, 30, 8])
# assert not sat([10, 30, 8], target=70, max_stamps=4, options=[10, 30, 8])
# assert not sat([10, 30, 8, 10, 30, 8], target=160, max_stamps=6, options=[10, 30, 8, 10, 30, 8])
# assert not sat([10, 30, 8, 10, 30, 8, 10, 30, 8], target=320, max_stamps=8, options=[10, 30, 8,

if __name__ == "__main__":
    assert sat(sol())
