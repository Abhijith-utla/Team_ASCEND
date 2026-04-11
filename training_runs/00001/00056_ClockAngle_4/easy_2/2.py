def sat(hand_position: float):
    hour_angle = 30 * (hand_position[0] % 12) + (hand_position[1] / 12)
    minute_angle = 6 * (hand_position[1])
    return abs(hour_angle - minute_angle) < 2

def sol():
    hand_position = [0, 0]
    while not sat(hand_position):
        hand_position[0] += 0.1
        hand_position[1] += 0.1
    return hand_position

if __name__ == "__main__":
    assert sat(sol())
