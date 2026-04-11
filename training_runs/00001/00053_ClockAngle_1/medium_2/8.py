def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 <= h <= 23 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

assert sat([])
assert sat([0, 0])
assert not sat([13, 30])
assert not sat([23, 0])
assert not sat([12, 60])
assert not sat([20, 35])
assert sat([12, 30])
assert sat([12, 0])
assert sat([15, 45])
assert sat([18, 15])
assert not sat([22, 55])

if __name__ == "__main__":
    assert sat(sol())
