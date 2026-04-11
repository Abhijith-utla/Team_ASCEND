def sat(hands: List[int], target_angle=133):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# For verification:
assert sat([])
assert not sat([5, 30])
assert sat([12, 30])
assert not sat([12, 0])
assert sat([1, 1])
assert not sat([11, 55])
assert not sat([11, 0])
assert sat([12, 45])
assert not sat([12, 55])
assert sat([1, 59])
assert not sat([11, 5])
assert sat([23, 15])
assert not sat([23, 0])
assert sat([0, 1])
assert not sat([0, 59])
assert sat([11, 30])
assert not sat([12, 0])
assert sat([1, 30])
assert not sat([2, 30])
assert sat([11, 0])
assert not sat([11, 45])
assert sat([12, 15])
assert not sat([12, 3

if __name__ == "__main__":
    assert sat(sol())
