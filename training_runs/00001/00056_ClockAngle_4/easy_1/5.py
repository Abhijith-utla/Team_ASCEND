def sat(hand_position: float):
    hour_angle = 30 * (hand_position[0] % 12) + (hand_position[1] / 12)
    minute_angle = 6 * (hand_position[1])
    return abs(hour_angle - minute_angle) <= 1

def sol():
    hour_angle = 30 * (0 % 12) + (0 / 12)
    minute_angle = 6 * (0)
    return abs(hour_angle - minute_angle) <= 1

print(sol())

if __name__ == "__main__":
    assert sat(sol())
