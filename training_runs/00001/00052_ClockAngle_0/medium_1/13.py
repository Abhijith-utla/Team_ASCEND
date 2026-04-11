def sat(hands: Tuple[int, int]) -> bool:
    h, m = hands
    assert 0 <= h < 24 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return 12, 30

def sat(hands: Tuple[int, int]) -> bool:
    h, m = hands
    assert 0 <= h < 24 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    target_angle = 12
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

# Test the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
