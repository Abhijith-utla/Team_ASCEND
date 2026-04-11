def sat(hands: Tuple[int, int]):
    h, m = hands
    assert 0 <= h < 24 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [40, 359 - 40]

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
