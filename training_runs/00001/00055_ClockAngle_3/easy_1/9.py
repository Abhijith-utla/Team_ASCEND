def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2 - target_angle
    minute_angle = 6 * m - target_angle
    return hour_angle == 0 and minute_angle == 0

def sol():
    return []

# Test cases
assert sat([])
assert not sat([0, 0])
assert not sat([12, 0])
assert not sat([11, 59])
assert not sat([11, 60])
assert not sat([13, 0])
assert not sat([13, 30])
assert not sat([13, 45])
assert not sat([13, 59])
assert not sat([14, 0])
assert not sat([14, 30])
assert not sat([14, 45])
assert not sat([14, 59])
assert not sat([15, 0])
assert not sat([15, 30])
assert not sat([15, 45])
assert not sat([15, 59])
assert not sat([16, 0])
assert not sat([16, 30])
assert not sat([16, 45])
assert not sat([16, 59])
assert not sat([

if __name__ == "__main__":
    assert sat(sol())
