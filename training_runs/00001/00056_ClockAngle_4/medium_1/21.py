def sat(hand_position: float, target_angle = 68):
    hour_angle = 30 * (hand_position[0] % 12) + (hand_position[1] / 12)
    minute_angle = 6 * (hand_position[1])
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
