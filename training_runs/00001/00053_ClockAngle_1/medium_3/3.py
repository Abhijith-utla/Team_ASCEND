def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 <= h < 24 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

assert sat([])
assert not sat([0, 0])
assert not sat([23, 59])
assert sat([12, 0])
assert not sat([11, 59])
assert not sat([12, 0])
assert not sat([11, 59])
assert not sat([12, 1])
assert sat([12, 1])
assert not sat([11, 61])
assert not sat([11, 60])

if __name__ == "__main__":
    assert sat(sol())
