def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

assert sat([])
assert not sat([6, 0])
assert not sat([12, 30])
assert not sat([12, 45])
assert not sat([1, 59])
assert not sat([13, 0])
assert not sat([11, 0])
assert not sat([11, 30])
assert sat([12, 30])
assert sat([1, 30])
assert sat([1, 0])
assert not sat([0, 0])
assert not sat([11, 60])
assert not sat([23, 0])
assert not sat([23, 30])
assert not sat([9, 30])
assert not sat([9, 0])
assert not sat([22, 30])
assert not sat([22, 0])
assert not sat([10, 60])
assert sat([10, 0])
assert not sat([8, 0])
assert not sat([8, 30])

if __name__ == "__main__":
    assert sat(sol())
