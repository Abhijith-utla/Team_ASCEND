def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Example usage:
# assert sat([])
# assert sat([37])
# assert sat([37, 37])
# assert sat([37, 37, 12])
# assert sat([37, 37, 12, 87])
# assert sat([37, 37, 12, 87, 39])
# assert not sat([37, 37, 12, 87, 39, 39])
# assert not sat([37, 37, 12, 87, 39])
# assert not sat([37, 37, 12, 87, 39, 39, 39, 39])

# This test case is for an empty list, which has zero stamps. The sum should be zero, the length should be zero, and the result should be False.
assert sat([])

# This test case is for a list with a single stamp, which has one stamp and the sum

if __name__ == "__main__":
    assert sat(sol())
