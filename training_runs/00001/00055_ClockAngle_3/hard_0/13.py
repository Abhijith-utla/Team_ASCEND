def sat(hands: List[int], target_angle=138):
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
assert not sat([11, 59])
assert sat([11, 30])
assert not sat([11, 0])
assert not sat([13, 0])
assert sat([1, 0])
assert not sat([1, 30])
assert not sat([2, 30])
assert sat([2, 0])
assert not sat([23, 0])
assert not sat([2, 60])
assert sat([2, 30])
assert not sat([3, 30])
assert not sat([4, 30])
assert sat([4, 0])
assert not sat([5, 0])
assert sat([5, 30])
assert not sat([6, 30])
assert not sat([7, 30])
assert sat([7, 0])
assert not sat([8, 0])
assert sat([

if __name__ == "__main__":
    assert sat(sol())
