def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle

def sol():
    return [0, 0]

# Testing the solution
assert sat(sol())

# Checking for a solution that doesn't meet the conditions
assert not sat([12, 30])
assert not sat([12, 31])
assert not sat([13, 0])
assert not sat([13, 30])
assert not sat([14, 0])
assert not sat([23, 59])

# Checking for a solution that meets the conditions
assert sat([12, 0])
assert sat([12, 30])
assert sat([12, 45])
assert sat([13, 30])
assert sat([15, 0])
assert sat([23, 30])
assert sat([23, 45])

if __name__ == "__main__":
    assert sat(sol())
