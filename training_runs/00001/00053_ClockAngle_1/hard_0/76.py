def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return [], 0

# This test should pass
assert sat(sol())

# This test should fail
assert not sat([12, 0])

# This test should fail
assert not sat([11, 59])

# This test should pass
assert sat([11, 30])

# This test should pass
assert sat([11, 0])

# This test should fail
assert not sat([1, 30])

# This test should fail
assert not sat([12, 59])

# This test should fail
assert not sat([1, 0])

# This test should pass
assert sat([1, 1])

# This test should fail
assert not sat([12, 1])

# This test should pass
assert sat([12, 30])

# This test should fail
assert not sat([13, 0])

# This test should fail
assert not sat([0, 30])

# This test should fail
assert not sat([0, 0])

#

if __name__ == "__main__":
    assert sat(sol())
