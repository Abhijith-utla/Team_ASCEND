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
assert not sat([0, 60])
assert not sat([11, 59])
assert sat([12, 30])
assert sat([1, 31])
assert not sat([13, 1])
assert not sat([1, 1])
assert sat([11, 30])
assert sat([12, 15])
assert not sat([1, 20])
assert not sat([13, 45])
assert sat([12, 45])
assert not sat([12, 140])
assert not sat([13, 15])
assert sat([1, 59])

if __name__ == "__main__":
    assert sat(sol())
