def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle

def sol():
    return []

# Test cases
assert sat([])
assert not sat([12, 0])
assert not sat([11, 59])
assert sat([11, 30])
assert sat([12, 30])
assert not sat([12, 0])
assert not sat([0, 0])
assert not sat([13, 0])
assert sat([1, 1])
assert sat([11, 1])
assert not sat([11, 40])
assert not sat([12, 40])
assert sat([11, 45])
assert sat([12, 45])
assert not sat([12, 50])
assert sat([11, 55])
assert sat([12, 55])
assert not sat([12, 59])

# Final checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
