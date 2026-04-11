def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return {}

# You can then use the sol function with the correct values to assert the correctness of the program.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
