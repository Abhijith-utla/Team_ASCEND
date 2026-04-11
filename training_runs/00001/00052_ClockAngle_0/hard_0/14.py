def sat(hands: List[int], target_angle=45):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# Test cases
assert sat([12, 0]) == True
assert sat([12, 30]) == True
assert sat([12, 45]) == False
assert sat([1, 30]) == False
assert sat([0, 0]) == False
assert sat([12, 60]) == True
assert sat([0, 60]) == False
assert sat([1, 1]) == False
assert sat([11, 55]) == True
assert sat([11, 0]) == True
assert sat([10, 30]) == False
assert sat([10, 45]) == False
assert sat([9, 30]) == True
assert sat([9, 45]) == False
assert sat([8, 30]) == False
assert sat([8, 45]) == True
assert sat([7, 30]) == False
assert sat([7, 45]) == True
assert sat([6, 30]) == False
assert sat([6, 45]) == True

if __name__ == "__main__":
    assert sat(sol())
