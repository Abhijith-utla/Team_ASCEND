def sat(hands: List[int], target_angle=133):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# Write your solution here

# This test case will pass if the function `sol` correctly solves the problem.
# You can add more test cases as you see fit.
assert sat(sol())
assert not sat([])
assert not sat([0, 0])
assert sat([12, 0])
assert sat([12, 30])
assert not sat([12, 60])
assert sat([12, 90])
assert sat([12, 120])
assert sat([12, 180])
assert not sat([12, 210])
assert sat([12, 270])
assert sat([12, 300])
assert not sat([13, 0])
assert not sat([13, 30])
assert not sat([13, 60])
assert not sat([14, 0])
assert not sat([14, 30])
assert not sat([14, 60])
assert not sat([23, 0])

if __name__ == "__main__":
    assert sat(sol())
