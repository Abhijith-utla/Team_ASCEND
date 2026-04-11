def sat(hands: Tuple[int, int], target_angle=133) -> bool:
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle

def sol():
    return 12, 30

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
