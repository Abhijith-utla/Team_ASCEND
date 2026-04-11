def sat(hands: Union[int, Tuple[int, int]], target_angle=39) -> bool:
    if isinstance(hands, int):
        h, m = hands, 0
    else:
        h, m = hands
    assert 0 <= h <= 23 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return 0, 0

if __name__ == "__main__":
    assert sat(sol())
