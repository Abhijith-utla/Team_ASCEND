def sat(hands: Tuple[int, int], target_angle=39) -> bool:
    h, m = hands
    assert 0 <= h <= 23 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return 12, 30

# Test cases
assert sat(sol())
assert not sat((12, 59))
assert not sat((23, 59))
assert not sat((12, 60))
assert sat((12, 30))
assert sat((2, 30))
assert not sat((0, 30))
assert not sat((11, 30))
assert not sat((12, 0))
assert not sat((23, 0))
assert not sat((0, 0))

if __name__ == "__main__":
    assert sat(sol())
