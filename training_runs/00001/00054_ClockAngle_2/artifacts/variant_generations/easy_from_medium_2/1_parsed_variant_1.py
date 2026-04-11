def sat(hands: List[int]):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle + minute_angle) == 133

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
