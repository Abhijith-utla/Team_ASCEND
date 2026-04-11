def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# Test Cases
assert sat([0, 0])
assert not sat([12, 0])
assert sat([6, 30])
assert sat([11, 30])
assert not sat([12, 30])
assert not sat([0, 30])
assert sat([9, 0])
assert not sat([11, 0])
assert not sat([11, 30])
assert sat([1, 57])
assert not sat([0, 57])
assert sat([12, 57])
assert not sat([0, 58])

if __name__ == "__main__":
    assert sat(sol())
