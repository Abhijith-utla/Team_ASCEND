def sat(hands: List[int], target_angle=45):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# test cases
assert sat([0, 0])
assert not sat([12, 0])
assert sat([12, 30])
assert sat([12, 35])
assert not sat([12, 55])
assert sat([2, 30])
assert sat([2, 45])
assert not sat([7, 0])
assert sat([7, 15])
assert sat([7, 30])
assert not sat([9, 0])
assert sat([9, 35])
assert not sat([9, 55])
assert sat([11, 15])
assert not sat([11, 30])
assert sat([11, 45])
assert not sat([11, 55])
assert sat([1, 45])
assert not sat([1, 55])
assert sat([2, 55])
assert not sat([2, 65])
assert sat([3, 30])
assert not sat([3, 45])

if __name__ == "__main__":
    assert sat(sol())
