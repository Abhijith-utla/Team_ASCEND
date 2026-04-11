def sat(hand_position: float):
    hour_angle = 30 * (hand_position[0] % 12) + (hand_position[1] / 12)
    minute_angle = 6 * (hand_position[1])
    return abs(hour_angle - minute_angle) < 3

def sol():
    return []

# Assuming 'hand_position' is a tuple of (hour, minute)
# The hour and minute values are normalized between 0 and 1
# Here we assume 'hand_position' is in radians
hand_position = (0.5, 0.66)
assert sat(hand_position)

if __name__ == "__main__":
    assert sat(sol())
