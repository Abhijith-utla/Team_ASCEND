def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# Test case
assert sat([])
assert not sat([0, 0])
assert not sat([12, 0])
assert sat([12, 30])
assert not sat([12, 59])
assert not sat([11, 0])
assert not sat([11, 30])
assert not sat([23, 0])
assert not sat([23, 30])
assert sat([1, 30])
assert not sat([2, 30])
assert sat([11, 59])
assert not sat([12, 60])
assert not sat([22, 0])
assert not sat([22, 59])
assert not sat([0, 60])
assert not sat([1, 60])
assert not sat([0, 70])
assert not sat([1, 70])
assert not sat([0, 150])
assert not sat([1, 150])
assert not sat([0, 210])

if __name__ == "__main__":
    assert sat(sol())
