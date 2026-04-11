def sat(hands: List[int], target_angle=133):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

assert sat([])
assert not sat([0, 0])
assert not sat([12, 0])
assert sat([11, 30])
assert not sat([11, 45])
assert sat([12, 0])
assert sat([12, 30])
assert sat([11, 45])
assert not sat([13, 0])
assert not sat([11, 70])
assert sat([11, 110])
assert not sat([11, 150])
assert sat([12, 15])
assert not sat([12, 75])
assert not sat([13, 30])
assert not sat([13, 45])
assert not sat([14, 0])
assert not sat([11, 2])
assert not sat([11, 7])
assert not sat([12, 33])
assert not sat([12, 48])
assert not sat([13, 33])
assert

if __name__ == "__main__":
    assert sat(sol())
