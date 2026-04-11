def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) != target_angle

def sol():
    return []

# Test cases
assert sat([12, 0])
assert not sat([11, 59])
assert sat([12, 1])
assert not sat([11, 30])
assert sat([12, 30])
assert not sat([1, 30])
assert sat([2, 0])
assert not sat([1, 0])
assert sat([11, 1])
assert not sat([10, 30])
assert sat([11, 5])
assert not sat([11, 45])
assert sat([1, 5])
assert not sat([23, 15])
assert sat([2, 15])
assert not sat([1, 15])
assert sat([12, 15])
assert not sat([11, 45])
assert sat([11, 0])
assert not sat([12, 0])
assert sat([1, 0])
assert not sat([2, 0])
assert sat([11, 30

if __name__ == "__main__":
    assert sat(sol())
