def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 12
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == 360 - target_angle

def sol():
    return []

# Test cases
assert sat([])
assert not sat([6, 0])
assert not sat([12, 30])
assert sat([12, 30])
assert not sat([1, 30])
assert not sat([12, 60])
assert sat([12, 60])
assert not sat([11, 55])
assert sat([11, 55])
assert not sat([12, 5])
assert sat([12, 5])
assert not sat([0, 5])
assert sat([0, 5])
assert not sat([13, 30])
assert sat([13, 30])
assert not sat([13, 60])
assert sat([13, 60])
assert not sat([14, 30])
assert sat([14, 30])
assert not sat([23, 30])
assert sat([23, 30])
assert not sat([23, 60])
assert sat([

if __name__ == "__main__":
    assert sat(sol())
