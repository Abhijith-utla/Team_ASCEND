def sat(hands: List[int], target_angle=68):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

assert sat([])
assert not sat([4, 0])
assert not sat([12, 30])
assert not sat([12, 0])
assert not sat([23, 45])
assert not sat([9, 25])
assert sat([12, 30])
assert sat([1, 59])
assert not sat([11, 59])
assert sat([1, 0])
assert not sat([11, 0])
assert sat([12, 0])
assert not sat([0, 0])
assert sat([1, 5])
assert not sat([12, 60])
assert sat([11, 55])
assert not sat([12, 55])
assert sat([12, 5])
assert not sat([24, 0])
assert sat([12, 45])
assert not sat([23, 55])
assert sat([12, 40])

if __name__ == "__main__":
    assert sat(sol())
