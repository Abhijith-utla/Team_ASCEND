def sat(hands: List[int], target_angle=68):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return [0, 0]

# Test cases
assert sat(sol())
assert sat(sol([12, 30]))
assert not sat(sol([11, 31]))
assert not sat(sol([1, 360]))
assert sat(sol([1, 0]))
assert not sat(sol([12, 0]))
assert sat(sol([12, 45]))
assert not sat(sol([12, 55]))
assert sat(sol([12, 30]))
assert not sat(sol([1, 360]))
assert sat(sol([11, 30]))
assert not sat(sol([11, 31]))
assert not sat(sol([23, 0]))
assert not sat(sol([1, 361]))

if __name__ == "__main__":
    assert sat(sol())
