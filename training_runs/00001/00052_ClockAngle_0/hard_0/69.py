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
assert sat([6, 30])
assert not sat([7, 31])
assert sat([11, 30])
assert not sat([12, 31])
assert sat([0, 30])
assert not sat([1, 31])
assert sat([9, 0])
assert not sat([10, 0])
assert sat([2, 30])
assert not sat([3, 31])
assert sat([1, 0])
assert not sat([2, 0])
assert sat([5, 30])
assert not sat([6, 31])
assert sat([7, 0])
assert not sat([8, 0])
assert sat([1, 45])
assert not sat([2, 46])
assert sat([10, 15])
assert not sat([11, 16])
assert sat([3, 45])
assert not sat([

if __name__ == "__main__":
    assert sat(sol())
