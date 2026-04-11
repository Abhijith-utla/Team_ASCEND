def sat(hand_position: float, target_angle = 68):
    hour_angle = 30 * (hand_position[0] % 12) + (hand_position[1] / 12)
    minute_angle = 6 * (hand_position[1])
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return [0, 0]

# Test cases
assert sat(sol())
assert sat([30, 0])
assert not sat([30.1, 0])
assert sat([12, 30])
assert sat([12, 0])
assert not sat([0, 30])
assert not sat([15, 0])
assert sat([12, 45])
assert sat([12, 90])
assert sat([12, 180])
assert sat([12, 270])
assert sat([12, 360])

if __name__ == "__main__":
    assert sat(sol())
