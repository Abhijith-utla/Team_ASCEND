def sat(hands: List[int], target_angle=39):
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
assert sat([12, 45]) == True
assert sat([12, 60]) == True
assert sat([12, 75]) == True
assert sat([12, 90]) == True
assert sat([12, 105]) == True
assert sat([12, 120]) == True
assert sat([12, 135]) == True
assert sat([12, 150]) == True
assert sat([12, 165]) == True
assert sat([12, 180]) == True
assert sat([12, 195]) == True
assert sat([12, 210]) == True
assert sat([12, 225]) == True
assert sat([12, 240]) == True
assert sat([12, 255]) == True
assert

if __name__ == "__main__":
    assert sat(sol())
