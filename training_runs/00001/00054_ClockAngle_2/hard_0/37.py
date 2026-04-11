def sat(hands: List[int], target_angle=133):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# Test cases
assert sat([0, 0]) == True
assert sat([12, 0]) == True
assert sat([12, 30]) == True
assert sat([12, 31]) == False
assert sat([12, 45]) == True
assert sat([2, 0]) == True
assert sat([11, 59]) == True
assert sat([12, 59]) == True
assert sat([13, 0]) == False
assert sat([0, 59]) == False
assert sat([23, 59]) == True
assert sat([11, 1]) == True
assert sat([10, 59]) == False
assert sat([11, 0]) == False
assert sat([15, 0]) == False

if __name__ == "__main__":
    assert sat(sol())
