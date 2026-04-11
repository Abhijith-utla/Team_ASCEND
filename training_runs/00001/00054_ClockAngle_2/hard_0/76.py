def sat(hands: List[int], target_angle=133):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# Testing
assert sat([])
assert not sat([5, 50])
assert not sat([11, 1])
assert sat([12, 0])
assert sat([1, 30])
assert not sat([1, 60])
assert sat([7, 20])
assert not sat([8, 0])
assert sat([2, 40])
assert sat([11, 30])
assert not sat([12, 40])
assert sat([1, 45])
assert not sat([2, 20])
assert sat([11, 20])
assert not sat([1, 65])
assert sat([7, 30])
assert not sat([8, 10])
assert sat([12, 15])
assert not sat([1, 55])
assert sat([6, 15])
assert not sat([7, 10])
assert sat([11, 10])
assert not sat([12, 10])
assert

if __name__ == "__main__":
    assert sat(sol())
