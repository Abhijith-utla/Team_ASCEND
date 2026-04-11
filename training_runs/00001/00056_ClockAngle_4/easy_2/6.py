def sat(hand_position: float):
    hour_angle = 30 * (hand_position[0] % 12) + (hand_position[1] / 12)
    minute_angle = 6 * (hand_position[1])
    return abs(hour_angle - minute_angle) < 2

def sol():
    return [0, 0]

if __name__ == "__main__":
    assert sat(sol())
