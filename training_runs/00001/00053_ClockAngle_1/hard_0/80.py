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
assert sat([12, 30])
assert not sat([12, 45])
assert sat([12, 90])
assert not sat([12, 120])
assert sat([12, 180])
assert not sat([12, 210])
assert sat([12, 270])
assert not sat([12, 300])
assert sat([2, 0])
assert not sat([11, 59])
assert sat([11, 110])
assert not sat([11, 120])
assert sat([11, 180])
assert not sat([11, 210])
assert sat([11, 270])
assert not sat([11, 300])
assert sat([23, 0])
assert not sat([1, 59])
assert sat([1, 11

if __name__ == "__main__":
    assert sat(sol())
