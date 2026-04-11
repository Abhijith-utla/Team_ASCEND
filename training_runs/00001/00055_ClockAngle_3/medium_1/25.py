def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return hour_angle == minute_angle

def sol():
    return []

# Test cases
assert sat([])
assert not sat([0, 0])
assert not sat([12, 0])
assert not sat([12, 30])
assert not sat([11, 59])
assert not sat([11, 60])
assert not sat([13, 0])
assert not sat([13, 30])
assert not sat([13, 31])
assert not sat([14, 0])
assert not sat([14, 30])
assert not sat([14, 31])
assert not sat([15, 0])
assert not sat([15, 30])
assert not sat([15, 31])
assert not sat([16, 0])
assert not sat([16, 30])
assert not sat([16, 31])
assert not sat([17, 0])
assert not sat([17, 30])
assert not sat([17, 31])
assert not sat([1

if __name__ == "__main__":
    assert sat(sol())
