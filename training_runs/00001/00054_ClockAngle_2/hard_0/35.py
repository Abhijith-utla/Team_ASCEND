def sat(hands: List[int], target_angle=133):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# Checker
assert not sat([])
assert not sat([0, 0])
assert not sat([12, 0])
assert not sat([12, 30])
assert not sat([11, 59])
assert not sat([11, 60])
assert sat([11, 30])
assert sat([1, 30])
assert sat([12, 30])
assert sat([2, 30])
assert sat([11, 58])
assert sat([11, 59])
assert sat([12, 0])
assert sat([12, 1])
assert sat([12, 29])
assert sat([12, 31])
assert sat([12, 60])
assert sat([23, 30])
assert sat([0, 30])
assert sat([0, 45])
assert sat([0, 55])
assert sat([5, 30])
assert sat([6, 30])
assert

if __name__ == "__main__":
    assert sat(sol())
