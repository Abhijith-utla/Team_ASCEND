def sat(hands: List[int], target_angle=133):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

assert sat([])
assert sat([0, 0])
assert not sat([12, 0])
assert sat([12, 30])
assert sat([12, 33])
assert sat([0, 30])
assert sat([11, 55])
assert not sat([11, 60])
assert not sat([13, 0])
assert not sat([13, 10])
assert not sat([23, 0])
assert sat([23, 10])
assert sat([23, 30])
assert not sat([9, 0])
assert not sat([9, 30])
assert sat([9, 33])

if __name__ == "__main__":
    assert sat(sol())
