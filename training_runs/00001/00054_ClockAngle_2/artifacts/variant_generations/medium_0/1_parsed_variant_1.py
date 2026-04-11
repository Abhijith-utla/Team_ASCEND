def sat(hands: List[int], target_angle=133):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    # If the difference between the angles is equal to target_angle, return True
    return abs(hour_angle - minute_angle) == target_angle

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
