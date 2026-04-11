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
assert not sat([0, 0])
assert not sat([12, 0])
assert sat([12, 30])
assert not sat([12, 45])
assert sat([12, 30])
assert not sat([11, 59])
assert sat([11, 59])
assert not sat([1, 0])
assert not sat([1, 1])
assert not sat([11, 0])
assert not sat([11, 1])
assert not sat([1, 1])
assert not sat([12, 1])
assert not sat([12, 2])
assert not sat([12, 3])
assert not sat([12, 4])
assert not sat([12, 5])
assert not sat([12, 6])
assert not sat([12, 7])
assert not sat([12, 8])
assert not sat([12, 9])
assert not sat([12,

if __name__ == "__main__":
    assert sat(sol())
