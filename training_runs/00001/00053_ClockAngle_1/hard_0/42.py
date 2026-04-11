def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

assert sat([])
assert not sat([0, 0])
assert sat([1, 30])
assert not sat([1, 45])
assert not sat([1, 31])
assert sat([12, 0])
assert not sat([13, 0])
assert not sat([11, 60])
assert sat([11, 55])
assert not sat([2, 35])
assert sat([2, 55])
assert not sat([11, 54])
assert sat([11, 56])
assert not sat([12, 0])
assert not sat([1, 60])
assert sat([1, 37])
assert not sat([12, 0])
assert sat([1, 38])
assert not sat([11, 60])
assert not sat([12, 1])
assert not sat([11, 59])
assert sat([12, 1])
assert not sat([12, 30])
assert

if __name__ == "__main__":
    assert sat(sol())
