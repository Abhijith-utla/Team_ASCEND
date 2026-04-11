def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return hour_angle == hour_angle - target_angle and minute_angle == minute_angle - target_angle

def sol():
    return []

# This is to verify the correctness of the code.
assert sat([]) == False
assert sat([4, 30]) == True
assert sat([12, 30]) == False
assert sat([11, 31]) == False
assert sat([12, 0]) == True
assert sat([1, 30]) == True
assert sat([11, 59]) == False
assert sat([11, 60]) == False
assert sat([0, 30]) == True
assert sat([0, 0]) == True
assert sat([1, 59]) == False
assert sat([2, 0]) == True
assert sat([23, 59]) == False
assert sat([23, 58]) == False
assert sat([11, 57]) == False
assert sat([11, 58]) == True
assert sat([0, 59]) == True
assert sat([0, 0]) == True

if __name__ == "__main__":
    assert sat(sol())
