def sat(hands: List[int], target_angle=45):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# Test cases
assert sat([0, 0])
assert not sat([12, 0])
assert sat([12, 30])
assert not sat([12, 31])
assert sat([12, 45])
assert not sat([12, 46])
assert sat([12, 60])
assert not sat([12, 61])
assert sat([2, 0])
assert not sat([2, 59])
assert sat([2, 45])
assert not sat([2, 46])
assert sat([3, 30])
assert not sat([3, 31])
assert sat([3, 45])
assert not sat([3, 46])
assert sat([4, 30])
assert not sat([4, 31])
assert sat([4, 45])
assert not sat([4, 46])
assert sat([5, 30])
assert not sat([5, 31])
assert sat([5, 45

if __name__ == "__main__":
    assert sat(sol())
