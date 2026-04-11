def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return hour_angle == hour_angle - target_angle and minute_angle == minute_angle - target_angle

def sol():
    return [], 0

if __name__ == "__main__":
    assert sat(sol())
