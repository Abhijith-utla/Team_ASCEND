def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2 - target_angle
    minute_angle = 6 * m - target_angle
    return hour_angle == 0 and minute_angle == 0

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
