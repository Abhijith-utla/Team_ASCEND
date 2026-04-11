def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle

def sol():
    return []

# This function sol() doesn't take any arguments and returns an empty list. The checker will fail because there's no arguments provided for hands in the function call sol().

if __name__ == "__main__":
    assert sat(sol())
