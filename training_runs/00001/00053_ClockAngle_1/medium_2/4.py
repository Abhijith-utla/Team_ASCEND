def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 <= h <= 23 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return [], 0

# Test cases
assert sat(sol())
assert not sat([12, 0])
assert not sat([11, 59])
assert sat([12, 30])
assert sat([0, 30])
assert not sat([0, 45])
assert not sat([1, 45])
assert sat([11, 30])
assert sat([11, 0])
assert not sat([23, 0])
assert not sat([23, 1])
assert sat([22, 0])
assert not sat([22, 1])
assert not sat([12, 1])
assert not sat([0, 1])
assert not sat([12, 15])
assert not sat([11, 15])
assert not sat([12, 45])
assert not sat([11, 45])

# Assertions
assert sat([h, m]) for h in range(24) for m in range(60)
assert 0 <= h <= 2

if __name__ == "__main__":
    assert sat(sol())
