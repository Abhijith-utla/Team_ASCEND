def sat(hands: Tuple[int, int]) -> bool:
    h, m = hands
    assert 0 < h < 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return (12, 0)

# This test case checks if the function works with a few different inputs
assert sat(sol())
assert sat((11, 59))
assert not sat((12, 0))
assert not sat((11, 60))
assert sat((12, 30))
assert not sat((11, 30))

# This test case checks if the function works with a few different possible angles
assert sat((10, 30))
assert sat((10, 45))
assert sat((10, 60))
assert sat((20, 45))
assert sat((20, 60))
assert sat((20, 30))
assert not sat((21, 30))
assert not sat((19, 30))
assert not sat((19, 45))
assert not sat((19, 60))
assert not sat((21, 45))
assert not sat((21, 60))

# This test case checks if the

if __name__ == "__main__":
    assert sat(sol())
