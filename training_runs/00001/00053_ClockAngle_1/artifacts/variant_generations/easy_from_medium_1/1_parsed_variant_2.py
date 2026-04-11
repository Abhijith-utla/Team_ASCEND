def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle or abs(hour_angle - minute_angle) == 360 - target_angle

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
